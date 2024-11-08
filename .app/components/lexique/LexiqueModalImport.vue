<template>
  <TairoModal :open="open" size="md" @close="close">
    <template #header>
      <div class="flex items-center justify-between p-4">
        <h3 class="font-heading text-muted-900 text-lg font-medium leading-6 dark:text-white">
          Importer un lexique
        </h3>
        <BaseButtonClose @click="close" />
      </div>
    </template>

    <div class="p-4">
      <div class="max-w-xl">
        <BaseInputFileHeadless
          v-slot="{ open, remove, preview, drop, files }"
          @change="handleFileSelect"
        >
          <!-- Controls -->
          <div
            role="button"
            tabindex="-1"
            @dragenter.stop.prevent
            @dragover.stop.prevent
            @drop="drop"
          >
            <div
              v-if="!files?.length"
              class="nui-focus border-muted-300 dark:border-muted-700 hover:border-muted-400 focus:border-muted-400 dark:hover:border-muted-600 dark:focus:border-muted-700 group cursor-pointer rounded-lg border-[3px] border-dashed p-8 transition-colors duration-300"
              tabindex="0"
              role="button"
              @click="open"
              @keydown.enter.prevent="open"
            >
              <div class="p-5 text-center">
                <Icon
                  name="mdi-light:cloud-upload"
                  class="text-muted-400 group-hover:text-primary-500 group-focus:text-primary-500 mb-2 size-10 transition-colors duration-300"
                />
                <h4 class="text-muted-400 font-sans text-sm">
                  Déposez le fichier à télécharger
                </h4>
                <div>
                  <span class="text-muted-400 font-sans text-[0.7rem] font-semibold uppercase">
                    Ou
                  </span>
                </div>
                <label
                  for="file"
                  class="text-muted-400 group-hover:text-primary-500 group-focus:text-primary-500 cursor-pointer font-sans text-sm underline underline-offset-4 transition-colors duration-300"
                >
                  Sélectionner le fichier
                </label>
              </div>
            </div>

            <ul v-else class="mt-6 space-y-2">
              <li v-for="file in files" :key="file.name">
                <div
                  class="border-muted-200 dark:border-muted-700 dark:bg-muted-800 relative flex items-center justify-end gap-2 rounded-xl border bg-white p-3"
                >
                  <div class="flex justify-center items-center gap-2">
                    <div class="font-sans">
                      <span class="text-muted-800 dark:text-muted-100 line-clamp-1 block text-sm">
                        {{ file.name }}
                      </span>
                      <span class="text-muted-400 block text-xs">
                        {{ formatFileSize(file.size) }}
                      </span>
                    </div>
                  </div>

                  <div class="flex gap-2">
                    <button
                      class="border-muted-200 hover:border-primary-500 text-muted-700 dark:text-muted-200 hover:text-primary-600 dark:border-muted-700 dark:bg-muted-900 dark:hover:border-primary-500 dark:hover:text-primary-600 relative flex size-8 cursor-pointer items-center justify-center rounded-full border bg-white transition-colors duration-300"
                      type="button"
                      tooltip="Remove"
                      @click.prevent="remove(file)"
                    >
                      <Icon name="lucide:x" class="size-4" />
                      <span class="sr-only">Remove</span>
                    </button>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </BaseInputFileHeadless>
      </div>
    </div>

    <template #footer>
      <div class="flex justify-end gap-2 p-4">
        <BaseButton @click="close">Annuler</BaseButton>
        <BaseButton @click="handleFileUpload">Importer</BaseButton>
      </div>
    </template>
  </TairoModal>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const selectedFile = ref<File | null>(null);
const props = defineProps({
  open: Boolean,
});
const emits = defineEmits(['close', 'importedData']);

const close = () => emits('close');

function handleFileSelect(event: Event) {
  selectedFile.value = (event.target as HTMLInputElement).files?.[0] || null;
}

function handleFileUpload() {
  if (selectedFile.value) {
    const reader = new FileReader();
    
    // Use readAsText with the correct encoding
    reader.readAsText(selectedFile.value, 'UTF-8'); // Specify UTF-8 encoding

    reader.onload = () => {
      const text = reader.result as string;
      parseCSV(text);
    };
  }
}

function parseCSV(data: string) {
  const rows : string[]= data.split('\n');
  const parsedData: Array<Record<string, any>> = rows.slice(1).map((row) => {
    // Remove double quotes and split by semicolon
    const cleanedRow = row.replace(/"/g, ''); // Remove quotes
    const [title, description] = cleanedRow.split(';').map(item => item.trim()); // Split by semicolon
    return { title, description: description || '' }; // Ensure description is an empty string if undefined
  });
  
  // Filter out any rows that don't have a title
  const validData = parsedData.filter(item => item.title);

  postLexiques(validData); // Call postLexiques directly after parsing
}

async function postLexiques(parsedData : Array<Record<string, any>>) {
  try {
    const response = await fetch('/api/v1/lexique', { // Call the new Nuxt API endpoint
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(parsedData),
    });

    if (!response.ok) {
      throw new Error('Failed to import lexiques');
    }

    const importedLexiques = await response.json();
    emits('importedData', importedLexiques); // Emit the imported lexiques
    close();
  } catch (error) {
    console.error('Error importing lexiques:', error);
  }
}
</script>
