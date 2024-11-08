<script setup lang="ts">
definePageMeta({
  preview: {
    title: 'User',
    description: 'For viewing user info',
    categories: ['layouts', 'lists'],
    src: '/img/screens/layouts-user.png',
    srcDark: '/img/screens/layouts-user-dark.png',
    order: 30,
    new: true,
  },
})

const id: string = "1";
const userData = ref<any>(null);

async function fetchUser() {
  try {
    const response = await fetch(`/api/v1/profil/${id}`);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    userData.value = await response.json();
    console.log(userData.value)
  } catch (error) {
    console.error('Error fetching user data:', error);
    userData.value = null; // Optional: set userData to null on error
  }
}

onMounted(() => {
  fetchUser();
});
</script>

<template>
  <div>
    <NuxtLayout>
      <div v-if="!userData" class="w-full flex justify-center items-center">
        <BaseSpinner /> <!-- You can use a spinner component or create your own loading indicator -->
      </div>
      <div v-else class="w-full">
        <!--Header-->
        <div class="border-muted-200 dark:border-muted-800 border-b py-6 flex flex-row items-center gap-[39vw]">
          <div class="flex items-center gap-3">
            <BaseAvatar size="2xl" :src="`http://127.0.0.1:5000/${userData.user.photo}`"  rounded="none" mask="blob" />

            <div>
              <BaseHeading as="h2" size="2xl" weight="medium" lead="tight" class="text-muted-800 dark:text-white">
                {{ userData.user.firstname }} {{ userData.user.lastname }}
              </BaseHeading>
              <BaseParagraph size="md" class="text-muted-500 dark:text-muted-400">
                {{ userData.user.email }}
              </BaseParagraph>
            </div>
            
          </div>
          <BaseThemeSwitch />
        </div>
        <!--Content-->
        <div class="space-y-7">
          <!--Section-->
          <div class="grid gap-8 pt-6 md:grid-cols-12">
            <!--Column-->
            <div class="md:col-span-5">
              <div class="w-full max-w-md">
                <BaseHeading as="h3" size="3xl" weight="medium" class="text-muted-800 dark:text-muted-100 mb-1">
                  Informations générales
                </BaseHeading>
              </div>
            </div>
            <!--Column-->
            <div class="md:col-span-7">

              <div class="divide-muted-200 dark:divide-muted-800 flex flex-col divide-y">
                <div class="group">
                  <div
                    class="font-heading text-muted-600 dark:text-muted-400 hover:bg-muted-200 dark:hover:bg-muted-700 flex items-center gap-4 p-4 text-sm transition-colors duration-300">
                    <div>
                      <BaseHeading as="h3" size="md" weight="medium" class="text-muted-400">
                        Civilité
                      </BaseHeading>
                      <BaseText class="dark:text-slate-200" size="lg">
                        {{ userData.user.civility.title }}
                      </BaseText>
                    </div>

                  </div>
                </div>
                <!--Item-->
                <div class="group">
                  <div
                    class="font-heading text-muted-600 dark:text-muted-400 hover:bg-muted-200 dark:hover:bg-muted-700 flex items-center gap-4 p-4 text-sm transition-colors duration-300">
                    <div>
                      <BaseHeading as="h3" size="md" weight="medium" class="text-muted-400">
                        Nom
                      </BaseHeading>
                      <BaseText class="dark:text-slate-200" size="lg">
                        {{ userData.user.lastname }}
                      </BaseText>
                    </div>

                  </div>
                </div>
                <!--Item-->
                <div class="group">
                  <div
                    class="font-heading text-muted-600 dark:text-muted-400 hover:bg-muted-200 dark:hover:bg-muted-700 flex items-center gap-4 p-4 text-sm transition-colors duration-300">
                    <div>
                      <BaseHeading as="h3" size="md" weight="medium" class="text-muted-400">
                        Prénom
                      </BaseHeading>
                      <BaseText class="dark:text-slate-200" size="lg">
                        {{ userData.user.firstname }}
                      </BaseText>
                    </div>

                  </div>
                </div>
                <!--Item-->
                <div class="group">
                  <div
                    class="font-heading text-muted-600 dark:text-muted-400 hover:bg-muted-200 dark:hover:bg-muted-700 flex items-center gap-4 p-4 text-sm transition-colors duration-300">
                    <div>
                      <BaseHeading as="h3" size="md" weight="medium" class="text-muted-400">
                        Identifiant
                      </BaseHeading>
                      <BaseText class="dark:text-slate-200" size="lg">
                        {{ userData.user.username }}
                      </BaseText>
                    </div>

                  </div>
                </div>

                <div class="group">
                  <div
                    class="font-heading text-muted-600 dark:text-muted-400 hover:bg-muted-200 dark:hover:bg-muted-700 flex items-center gap-4 p-4 text-sm transition-colors duration-300">
                    <div>
                      <BaseHeading as="h3" size="md" weight="medium" class="text-muted-400">
                        Email
                      </BaseHeading>
                      <BaseText class="dark:text-slate-200" size="lg">
                        {{ userData.user.email }}
                      </BaseText>
                    </div>

                  </div>
                </div>

                <div class="group">
                  <div
                    class="font-heading text-muted-600 dark:text-muted-400 hover:bg-muted-200 dark:hover:bg-muted-700 flex items-center gap-4 p-4 text-sm transition-colors duration-300">
                    <div>
                      <BaseHeading as="h3" size="md" weight="medium" class="text-muted-400">
                        Langue des E-mails
                      </BaseHeading>
                      <BaseText class="dark:text-slate-200" size="lg">
                        Français
                      </BaseText>
                    </div>

                  </div>
                </div>

                <div class="group">
                  <div
                    class="font-heading text-muted-600 dark:text-muted-400 hover:bg-muted-200 dark:hover:bg-muted-700 flex items-center gap-4 p-4 text-sm transition-colors duration-300">
                    <div>
                      <BaseHeading as="h3" size="md" weight="medium" class="text-muted-400">
                        Entreprise
                      </BaseHeading>
                      <BaseText class="dark:text-slate-200" size="lg">
                        {{ userData.user.laboratory.slug }}
                      </BaseText>
                    </div>

                  </div>
                </div>

              </div>
            </div>
          </div>
          <!--Section-->
          <div class="grid gap-8 pt-6 md:grid-cols-12">
            <!--Column-->
            <div class="md:col-span-5">
              <div class="w-full max-w-xs">
                <BaseHeading as="h3" size="3xl" weight="medium" class="text-muted-800 dark:text-muted-100 mb-1">
                  Superviseur
                </BaseHeading>
              </div>
            </div>
            <!--Column-->
            <div class="md:col-span-7">
              <div class="divide-muted-200 dark:divide-muted-800 flex flex-col divide-y">
                <div class="group">
                </div>
                <div class="group">
                  <div
                    class="font-heading text-muted-600 dark:text-muted-400 hover:bg-muted-200 dark:hover:bg-muted-700 flex items-center gap-4 p-4 text-sm transition-colors duration-300">
                    
                    <BaseList v-for="(supervisor, index) in userData.supervisors" :key="index">
                      <div class="flex flex-row items-center gap-[1vh]">
                      <BaseAvatar size="lg" :src="`http://127.0.0.1:5000/${userData.user.photo}`"/>
                      <BaseListItem :title="`${supervisor.lastname} ${supervisor.firstname} (${supervisor.username})`" >        
                      </BaseListItem>
                    </div>
                    </BaseList>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- aPPRENANT SUIVIS  -->
          <div class="grid gap-8 pt-6 md:grid-cols-12">
            <!--Column-->
            <div class="md:col-span-5">
              <div class="w-full max-w-xs">
                <BaseHeading as="h3" size="3xl" weight="medium" class="text-muted-800 dark:text-muted-100 mb-1">
                  Apprenant suivis
                </BaseHeading>
              </div>
            </div>
            <!--Column-->
            <div class="md:col-span-7">
              <div class="divide-muted-200 dark:divide-muted-800 flex flex-col divide-y">
                <div class="group">
                </div>
                <div class="group">
                  <div
                    class=" font-heading text-muted-600 dark:text-muted-400 hover:bg-muted-200 dark:hover:bg-muted-700 flex flex-col justify-start gap-4 p-4 text-sm transition-colors duration-300">
                    <BaseList v-for="(student, index) in userData.students" :key="index">
                      <div class="flex flex-row items-center gap-[1vh]">
                      <BaseAvatar size="lg" :src="`http://127.0.0.1:5000/${userData.user.photo}`" />
                      <BaseListItem :title="`${student.lastname} ${student.firstname} (${student.username})`" >        
                      </BaseListItem>
                    </div>
                    </BaseList>
                    
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- gROUP -->

          <div class="grid gap-8 pt-6 md:grid-cols-12">
            <!--Column-->
            <div class="md:col-span-5">
              <div class="w-full max-w-xs">
                <BaseHeading as="h3" size="3xl" weight="medium" class="text-muted-800 dark:text-muted-100 mb-1">
                  Groupe(s)
                </BaseHeading>
              </div>
            </div>
            <!--Column-->
            <div class="md:col-span-7">
              <div class="divide-muted-200 dark:divide-muted-800 flex flex-col divide-y">
                <div class="group">
                </div>
                <div class="group">
                  <div
                    class="font-heading text-muted-600 dark:text-muted-400 hover:bg-muted-200 dark:hover:bg-muted-700 flex items-center gap-4 p-4 text-sm transition-colors duration-300">

                    <BaseList>
                      <li>
                        <BaseText class="dark:text-slate-200" size="lg">
                          {{ userData.user.group.name }}
                        </BaseText>
                      </li>
                    </BaseList>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </NuxtLayout>
  </div>
</template>
