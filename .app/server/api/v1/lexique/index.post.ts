import { defineEventHandler, readBody } from 'h3';

export default defineEventHandler(async (event) => {
  // Get the parsed data from the request body
  const body = await readBody(event);
  
  try {
    const response = await fetch('http://localhost:5000/api/v1/lexique', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body), // Send the body data
    });

    if (!response.ok) {
      throw new Error('Failed to import lexiques');
    }

    const importedLexiques = await response.json();
    return importedLexiques; // Return the imported lexiques
  } catch (error) {
    console.error('Error importing lexiques:', error);
    return { success: false, error: 'Error importing lexiques' };
  }
});
