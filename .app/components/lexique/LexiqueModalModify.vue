<template>
  <TairoModal :open="isOpen" size="md" @close="closeModal">
    <template #header>
      <div class="flex w-full items-center justify-between p-4 md:p-6">
        <h3 class="font-heading text-3xl font-medium leading-6">
          Modifier le lexique
        </h3>
        <BaseButtonClose @click="closeModal" />
      </div>
    </template>

    <div class="p-4 md:p-6">
    <div class="mx-auto w-full max-w-xs text-center">
      <label class="text-lg font-semibold flex justify-start" for="title-input">Titre</label>
      <BaseInput
        id="title-input"
        rounded="md"
        :modelValue="editableLexique ? editableLexique.title : ''" 
        @update:modelValue="(value) => { if (editableLexique) editableLexique.title = value }"
      />
      <label class="text-lg font-semibold mt-[2vh] flex justify-start" for="description-input">Description</label>
      <BaseTextarea
        id="description-input"
        rounded="md"
        color-focus
        :modelValue="editableLexique ? editableLexique.description : ''" 
        @update:modelValue="(value) => { if (editableLexique) editableLexique.description = value }"
      />
    </div>
  </div>

    <template #footer>
      <div class="p-4 md:p-6">
        <div class="flex gap-x-2">
          <BaseButton @click="closeModal">Annuler</BaseButton>
          <BaseButton color="primary" variant="solid" @click="confirmEdit">Confirmer</BaseButton>
        </div>
      </div>
    </template>
  </TairoModal>
</template>

<script setup lang="ts">
import { ref, defineProps, defineEmits, watch } from 'vue';

// Props for modal visibility and selected lexique data
const props = defineProps({
  lexiqueData: Object,
  isOpen: Boolean,
});



// Emits for closing and confirming changes
const emit = defineEmits(['close', 'confirm']);

// Local copy of lexique data to edit within modal
const editableLexique = ref<Record<string, any> | null>(null);

// Watch prop changes to update local data copy
watch(
  () => props.lexiqueData,
  (newData) => {
    if (newData) {
      editableLexique.value = {
        ...newData, // Spread to retain other properties
        title: newData.title, // Update title
        description: newData.description, // Update description
      } as Record<string, any>; // Cast as Record
    }
  },
  { immediate: true }
);

function closeModal() {
  emit('close');
}

function confirmEdit() {
  emit('confirm', editableLexique.value);
  closeModal();
}
</script>