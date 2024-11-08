import { defineEventHandler } from 'h3';

export default defineEventHandler(async (event) => {
  try {
    const response = await fetch('http://localhost:5000/api/v1/lexique');
    
    if (!response.ok) {
      throw new Error('Failed to fetch lexiques');
    }

    const data = await response.json();
    return data; // Return the data directly to the client
  } catch (error) {
    console.error('Error fetching lexiques:', error);
    return { success: false, error: 'Error fetching lexiques' };
  }
});