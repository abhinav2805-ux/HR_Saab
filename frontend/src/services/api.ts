import axios from 'axios';

// Base URL for API
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://hr-saab.onrender.com';

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Resume services
export const resumeService = {
  uploadResume: async (file: File) => {
    try {
      const formData = new FormData();
      formData.append('resume', file);
      
      const response = await api.post('/parse-resume', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      
      return response.data;
    } catch (error) {
      console.error('Resume upload error:', error);
      if (error.response) {
        throw new Error(`Server error: ${error.response.data?.error || error.response.statusText}`);
      } else if (error.request) {
        throw new Error('No response from server. Please check your connection.');
      } else {
        throw new Error(`Request failed: ${error.message}`);
      }
    }
  },
};

// Interview services
export const interviewService = {
  startInterview: async (resumeData: any) => {
    try {
      const response = await api.post('/start-interview', { resumeData });
      
      // Transform backend response to frontend expected format
      return {
        interviewId: response.data.interviewId,
        question: response.data.message,  // Map 'message' to 'question'
        interviewStatus: response.data.interviewStatus
      };
    } catch (error) {
      console.error('Error starting interview:', error);
      if (error.response) {
        throw new Error(`Server error: ${error.response.data?.error || error.response.statusText}`);
      } else if (error.request) {
        throw new Error('No response from server. Please check your connection.');
      } else {
        throw new Error(`Request failed: ${error.message}`);
      }
    }
  },
  
  continueInterview: async (interviewId: string, userResponse: string, resumeData: any, conversationHistory: any[]) => {
    try {
      const response = await api.post('/continue-interview', {
        interviewId,
        userResponse,
        resumeData,
        conversationHistory,
      });
      
      return {
        question: response.data.message,  // Map 'message' to 'question'
        interviewStatus: response.data.interviewStatus,
        feedback: response.data.feedback,
        score: response.data.score,
        lowScoreStreak: response.data.lowScoreStreak
      };
    } catch (error) {
      console.error('Error continuing interview:', error);
      if (error.response) {
        throw new Error(`Server error: ${error.response.data?.error || error.response.statusText}`);
      } else if (error.request) {
        throw new Error('No response from server. Please check your connection.');
      } else {
        throw new Error(`Request failed: ${error.message}`);
      }
    }
  },
};

// Add response interceptor to handle errors
api.interceptors.response.use(
  (response) => response.data,
  (error) => {
    if (error.response) {
      // Server responded with a status code outside 2xx
      console.error('API Error:', error.response.data);
      return Promise.reject(error.response.data.error || 'API request failed');
    } else if (error.request) {
      // No response received
      console.error('No response received:', error.request);
      return Promise.reject('No response from server');
    } else {
      // Something happened in setting up the request
      console.error('Request setup error:', error.message);
      return Promise.reject('Request setup failed');
    }
  }
);

export default api;