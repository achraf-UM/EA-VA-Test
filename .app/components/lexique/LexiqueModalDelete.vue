<template>
    <TairoModal :open="open" size="sm" @close="close">
      <template #header>
        <div class="flex items-center justify-between p-4">
          <h3 class="font-heading text-2xl  font-medium leading-6 ">
            Confirmer la suppression
          </h3>
          <BaseButtonClose @click="close" />
        </div>
      </template>
  
      <div class="p-4">
        <p>Êtes-vous sûr de vouloir supprimer ce lexique ?</p>
      </div>
  
      <template #footer>
        <div class="flex justify-end gap-2 p-4">
          <BaseButton @click="close">Annuler</BaseButton>
          <BaseButton color="danger" variant="solid" @click="confirmDelete">Supprimer</BaseButton>
        </div>
      </template>
    </TairoModal>
  </template>
  
  <script setup lang="ts">
  import { defineProps, defineEmits } from 'vue';
  
  const props = defineProps({
    open: Boolean,
  });
  
  const emits = defineEmits(['close', 'confirm']);
  
  const close = () => emits('close');
  const confirmDelete = () => emits('confirm');
  </script>
  