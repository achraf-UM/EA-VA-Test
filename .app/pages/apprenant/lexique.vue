<script setup lang="ts">
const app = useAppConfig()

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

const lexiques = ref<Card[]>([]);


const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('')

const selectedLetter = ref('')

const filteredCards = computed(() => {
    return selectedLetter.value
        ? lexiques.value.filter((lexique) =>
            lexique.title.startsWith(selectedLetter.value)
        )
        : lexiques.value
})

// Function to select letter
const selectLetter = (letter: string) => {
    selectedLetter.value = letter
}

const showAll = () => {
    selectedLetter.value = ''
}

async function fetchLexiques() {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/v1/lexique');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data: Card[] = await response.json(); // Ensure it's treated as an array of Card
    lexiques.value = data; // Update the lexiques with fetched data
    console.log(data)
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
    <div>
        <NuxtLayout>
            <div class="flex flex-row items-center gap-[55vw]">
                <BaseHeading as="h3" size="5xl" weight="bold" class="mb-[2vh]">Lexique</BaseHeading>
                <BaseThemeSwitch />
            </div>
            <div class="flex flex-wrap gap-2 justify-center mb-[3vh]">
                <button v-for="letter in alphabet" :key="letter" @click="selectLetter(letter)"
                    class="px-3 py-1 border rounded-lg"
                    :class="{ 'bg-blue-500 text-white': letter === selectedLetter }">
                    {{ letter }}
                </button>

                <BaseButtonIcon v-if="selectedLetter" @click="showAll" rounded="lg" color="warning">
        <Icon name="ph:list-bullets-bold" class="size-5" />
      </BaseButtonIcon>
  
            </div>

            <div
                class="grid w-full gap-[2vw] h-min-auto grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 mt-[3vh]">
                <div v-for="(card, index) in filteredCards" :key="index" class="flex">
                    <BaseCard :rounded="card.rounded" class="flex-grow p-6">
                        <BaseHeading as="h4" size="sm" weight="semibold" lead="tight"
                            class="text-muted-800 mb-2 dark:text-white">
                            {{ card.title }}
                        </BaseHeading>
                        <BaseParagraph size="sm" lead="tight" class="text-muted-400">
                            {{ card.description }}
                        </BaseParagraph>
                    </BaseCard>
                </div>
            </div>
        </NuxtLayout>
    </div>
</template>