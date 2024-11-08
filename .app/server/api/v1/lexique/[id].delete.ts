import { defineEventHandler, getQuery } from 'h3';

export default defineEventHandler(async (event) => {
  const { id } = event.context.params as { id: string | undefined };
  
  if (event.node.req.method === 'DELETE') {
    try {
      const response = await fetch(`http://localhost:5000/api/v1/lexique/${id}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error('Failed to delete lexique');
      }

      return { success: true };
    } catch (error) {
      console.error('Error deleting lexique:', error);
      return { success: false, error: 'Error deleting lexique' };
    }
  }
});
