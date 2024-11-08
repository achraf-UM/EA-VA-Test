// server/api/lexique/[id]/put.ts
import { defineEventHandler, readBody } from 'h3';



export default defineEventHandler(async (event) => {
  const { id } = event.context.params as { id: string | undefined };

  if (event.node.req.method === 'PUT') {
    const updatedLexique = await readBody(event); // Read the body of the request

    try {
      const response = await fetch(`http://localhost:5000/api/v1/lexique/${id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedLexique), // Send the updated lexique data
      });

      if (!response.ok) {
        throw new Error('Failed to update lexique');
      }

      const data = await response.json(); // Get the updated lexique data from the response
      return { success: true, data }; // Return success status and updated data
    } catch (error) {
      console.error('Error updating lexique:', error);
      return { success: false, error: 'Error updating lexique' };
    }
  }
});
