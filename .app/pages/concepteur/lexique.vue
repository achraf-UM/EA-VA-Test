<script setup lang="ts">
import { ref, computed } from 'vue';

interface Card {
    create_date: string;    
    description: string;     
    id: number;              
    is_valid: boolean;       
    revision: number;        
    title: string;           
    update_date: string;     
    uuid: string;
}

const lexiques = reactive<Card[]>([]);

const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
const selectedLetter = ref('');
const selectedLexique = ref<Card | null>(null);
const isModalOpen = ref(false);

const isDeleteModalOpen = ref(false);
const cardToDelete = ref<Card | null>(null);

const openDeleteModal = (lexique: Card) => {
  cardToDelete.value = lexique;
  isDeleteModalOpen.value = true;
};

async function deleteCard() {
  if (cardToDelete.value) {
    try {
      const response = await fetch(`/api/v1/lexique/${cardToDelete.value.id}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      // Remove the card from the local state if the deletion was successful
      lexiques.value = lexiques.value.filter((lexique) => lexique.id !== cardToDelete.value.id);
      cardToDelete.value = null; // Clear the card to delete
    } catch (error) {
      console.error('Error deleting card:', error);
    }
  }
  isDeleteModalOpen.value = false; // Close the delete modal
}

const filteredCards = computed(() => {
    return selectedLetter.value
        ? lexiques.value.filter((lexique) => lexique.title.startsWith(selectedLetter.value))
        : lexiques.value;
});

function selectLetter(letter: string) {
    selectedLetter.value = letter;
}

function showAll() {
    selectedLetter.value = '';
}

function openModal(lexique: Card) {
    selectedLexique.value = lexique;
    isModalOpen.value = true;
}

function closeModal() {
    isModalOpen.value = false;
}

async function updateLexique(updatedLexique: Card) {
    if (selectedLexique.value) {
        const index = lexiques.value.findIndex((lexique) => lexique.id === selectedLexique.value.id);
        if (index !== -1) {
            try {
              
              const response = await fetch(`/api/v1/lexique/${selectedLexique.value.id}`, {
                method: 'PUT',
                headers: {
                  'Content-Type': 'application/json',
                },
                body: JSON.stringify(updatedLexique), 
              });

                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                
                lexiques.value[index] = { ...updatedLexique };
            } catch (error) {
                console.error('Error updating lexique:', error);
            }
        }
    }
}

function appendLexiques(importedData : any) {
  lexiques.value.push(...importedData);
  lexiques.value = [...lexiques.value.sort((a, b) => a.title.localeCompare(b.title))];
}

function exportToCSV() {
  const header = "Title;Description"; 
  const rows = lexiques.value.map(lexique => 
    `"${lexique.title}";"${lexique.description}"` 
  );
  const csvContent = [header, ...rows].join("\n"); 

  const encodedUri = encodeURI(`data:text/csv;charset=utf-8,${csvContent}`);
  const link = document.createElement("a");
  link.setAttribute("href", encodedUri);
  link.setAttribute("download", "lexiques.csv");
  document.body.appendChild(link); // Required for FF

  link.click();
  document.body.removeChild(link); // Clean up
}

const isImportModalOpen = ref(false);

function openImportModal() {
  isImportModalOpen.value = true;
}


async function fetchLexiques() {
  try {
    const response = await fetch('/api/v1/lexique'); // Now this will call your new Nuxt API endpoint
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data: Card[] = await response.json();
    lexiques.value = data.sort((a, b) => a.title.localeCompare(b.title));
  } catch (error) {
    console.error('Error fetching lexiques:', error);
  }
}

// Fetch lexiques when the component is mounted
onMounted(() => {
  fetchLexiques();
});

</script>

<template>
  <NuxtLayout>
    <div class="flex flex-row items-center gap-[48vw]">
      <BaseHeading as="h3" size="5xl" weight="bold" class="mb-[2vh]">Lexique</BaseHeading>
      <BaseThemeSwitch />
    </div>
    <div class="flex flex-wrap gap-2 justify-center mb-[3vh]">
      <button
        v-for="letter in alphabet"
        :key="letter"
        @click="selectLetter(letter)"
        class="px-3 py-1 border rounded-lg"
        :class="{ 'bg-blue-500 text-white': letter === selectedLetter }"
      >
        {{ letter }}
      </button>
      <BaseButtonIcon v-if="selectedLetter" @click="showAll" rounded="lg" color="warning">
        <Icon name="ph:list-bullets-bold" class="size-5" />
      </BaseButtonIcon>
    </div>
    <div class="flex justify-end items-center gap-[3vh]">
    <BaseButton variant="outline" @click="exportToCSV" color="success">
      Exporter
    </BaseButton>

    <BaseButton variant="outline" color="info" @click="openImportModal">
    Importer
  </BaseButton>

  </div>

    <div class="grid w-full gap-[2vw] h-min-auto grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 mt-[3vh]">
  <div v-for="(card, index) in filteredCards" :key="index" class="flex">
    <BaseCard rounded="lg" class="flex flex-col flex-grow p-6"> <!-- Set flex column -->
      <div class="flex-grow"> <!-- Allow content to take available space -->
        <BaseHeading as="h4" size="sm" weight="semibold" lead="tight" class="text-muted-800 mb-2 dark:text-white">
          {{ card.title }}
        </BaseHeading>
        <BaseParagraph size="sm" lead="tight" class="text-muted-400">
          {{ card.description  }}
        </BaseParagraph>
      </div>
      <!-- Buttons container -->
      <div class="flex flex-row gap-[0.5vw] mt-[0.5vw] justify-end"> <!-- No need for items-end -->
        <BaseButtonIcon rounded="lg" color="info" @click="openModal(card)">
          <Icon name="ph:pen-duotone" class="size-5" />
        </BaseButtonIcon>
        <BaseButtonIcon rounded="lg" color="danger" @click="openDeleteModal(card)">
          <Icon name="ph:trash-duotone" class="size-5" />
        </BaseButtonIcon>
      </div>
    </BaseCard>
  </div>
</div>

    <!-- Delete Confirmation Modal -->
    <LexiqueModalDelete :open="isDeleteModalOpen" @close="isDeleteModalOpen = false" @confirm="deleteCard" />

    <!-- Lexique Modify Modal -->
    <LexiqueModalModify
      :isOpen="isModalOpen"
      :lexiqueData="selectedLexique"
      @close="closeModal"
      @confirm="updateLexique"
    />

    <LexiqueModalImport :open="isImportModalOpen" @close="isImportModalOpen = false" @importedData="appendLexiques"/>
  </NuxtLayout>
</template>
