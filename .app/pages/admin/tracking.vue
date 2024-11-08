<template>
    <NuxtLayout>
        <div class="w-full flex flex-col ">
            <div class="flex flex-row items-center gap-[48vw]">
                <BaseHeading as="h3" size="5xl" weight="bold" class="mb-[2vh]">Lexique</BaseHeading>
                <BaseThemeSwitch />
            </div>

            <TairoTable rounded="none">
                <template #header>
                    <TairoTableHeading uppercase class="p-4">
                        Statut
                    </TairoTableHeading>

                    <TairoTableHeading uppercase>
                        Date
                    </TairoTableHeading>

                    <TairoTableHeading uppercase>
                        Url
                    </TairoTableHeading>

                    <TairoTableHeading uppercase>
                        IP client
                    </TairoTableHeading>

                    <TairoTableHeading uppercase>
                        Utilisateur
                    </TairoTableHeading>

                    <TairoTableHeading uppercase class="p-4">
                        <span class="sr-only">View</span>
                    </TairoTableHeading>
                </template>

                <TairoTableRow v-for="member in team" :key="member.id">
                    <TairoTableCell class="p-4">
                        <div class="flex items-center">
                            <BaseCheckbox v-model="selected" :value="`table-1-${member.id}`" rounded="none"
                                color="primary" />
                        </div>
                    </TairoTableCell>

                    <TairoTableCell>
                        {{ member.name }}
                    </TairoTableCell>

                    <TairoTableCell light>
                        {{ member.expertise }}
                    </TairoTableCell>

                    <TairoTableCell>${{ member.rate }}/hour</TairoTableCell>

                    <TairoTableCell>
                        <BaseTag v-if="member.status === 'Available'" color="success" variant="pastel" rounded="full"
                            class="font-medium">
                            {{ member.status }}
                        </BaseTag>

                        <BaseTag v-else-if="member.status === 'New'" color="info" variant="pastel" rounded="full"
                            class="font-medium">
                            {{ member.status }}
                        </BaseTag>

                        <BaseTag v-else-if="member.status === 'Hired'" color="warning" variant="pastel" rounded="full"
                            class="font-medium">
                            {{ member.status }}
                        </BaseTag>
                    </TairoTableCell>

                    <TairoTableCell>
                        <a href="#"
                            class="text-primary-500 dark:text-primary-400 underline-offset-4 transition-opacity duration-300 hover:underline hover:opacity-75">
                            View
                        </a>
                    </TairoTableCell>
                </TairoTableRow>
            </TairoTable>
        </div>
    </NuxtLayout>
</template>

<script setup lang="ts">
const selected = ref([])
const selectAll = ref(false)

const team = [
    {
        id: 0,
        src: '/img/avatars/22.svg',
        name: 'Anna Vrinkof',
        role: 'UI/UX designer',
        expertise: 'UX Design',
        rate: 49,
        status: 'Available',
    },
    {
        id: 1,
        src: '/img/avatars/3.svg',
        name: 'John Cambell',
        role: 'Sales manager',
        expertise: 'Management',
        rate: 74,
        status: 'Hired',
    },
    {
        id: 2,
        src: '/img/avatars/9.svg',
        name: 'Beth Delanoe',
        role: 'Product designer',
        expertise: 'Product',
        rate: 43,
        status: 'Available',
    },
    {
        id: 3,
        src: '/img/avatars/14.svg',
        name: 'Andrew Higgs',
        role: 'Project manager',
        expertise: 'Project',
        rate: 69,
        status: 'New',
    },
]
</script>