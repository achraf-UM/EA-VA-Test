<script setup lang="ts">
import { toTypedSchema } from '@vee-validate/zod'
import { Field, useForm } from 'vee-validate'
import { z } from 'zod'

definePageMeta({
  layout: 'empty',
  title: 'Recover Password',
  preview: {
    title: 'Recover',
    description: 'For password recovery',
    categories: ['layouts', 'authentication'],
    src: '/img/screens/auth-recover.png',
    srcDark: '/img/screens/auth-recover-dark.png',
    order: 156,
  },
})

const VALIDATION_TEXT = {
  EMAIL_REQUIRED: 'A valid email is required',
}

// This is the Zod schema for the form input
// It's used to define the shape that the form data will have
const zodSchema = z.object({
  email: z.string().email(VALIDATION_TEXT.EMAIL_REQUIRED),
})

// Zod has a great infer method that will
// infer the shape of the schema into a TypeScript type
type FormInput = z.infer<typeof zodSchema>

const validationSchema = toTypedSchema(zodSchema)
const initialValues = {
  email: '',
} satisfies FormInput

const { handleSubmit, isSubmitting } = useForm({
  validationSchema,
  initialValues,
})

const success = ref(false)

// This is where you would send the form data to the server
const onSubmit = handleSubmit(async (values) => {
  // here you have access to the validated form values
  console.log('recover-success', values)

  try {
    // fake delay, this will make isSubmitting value to be true
    await new Promise(resolve => setTimeout(resolve, 4000))
  }
  catch {
    // discard errors
  }

  // always display success message
  success.value = true
})
</script>

<template>
  <div
    class="bg-muted-100 dark:bg-muted-900 relative min-h-screen w-full overflow-hidden px-4"
  >
    <div
      class="mx-auto flex h-16 w-full max-w-6xl items-center justify-between px-4"
    >
      <NuxtLink
        to="/dashboards"
        class="text-muted-400 hover:text-primary-500 dark:text-muted-700 dark:hover:text-primary-500 transition-colors duration-300"
      >
        <TairoLogo class="size-10" />
      </NuxtLink>
      <div>
        <BaseThemeToggle />
      </div>
    </div>
    <div class="flex w-full items-center justify-center">
      <div class="relative mx-auto w-full max-w-2xl">
        <!--Form-->
        <div class="me-auto ms-auto mt-4 w-full">
          <div class="me-auto ms-auto mt-4 w-full max-w-md">
            <div class="text-center">
              <BaseHeading
                as="h2"
                size="3xl"
                weight="normal"
                
              >
              Réinitialiser votre mot de passe
              </BaseHeading>
              <BaseParagraph size="sm" class="text-muted-400 mb-6">
                Suivez les instructions envoyées à votre adresse e-mail
              </BaseParagraph>
            </div>
            <Transition
              mode="out-in"
              enter-active-class="transition-all duration-300 ease-out"
              enter-from-class="scale-0 opacity-0"
              enter-to-class="scale-100 opacity-100"
              leave-active-class="transition-all duration-75 ease-in"
              leave-from-class="scale-100 opacity-100"
              leave-to-class="scale-0 opacity-0"
            >
              <div v-if="success" class="px-8 py-4">
                <div class="mb-4 space-y-4">
                  <BaseMessage class="p-6" :closable="false">
                    <p class="text-base">
                      Un e-mail vous a été envoyé avec des instructions sur la façon de réinitialiser votre mot de passe.
                    </p>

                    <small class="block pt-2">
                      Si vous ne recevez pas d'e-mail, veuillez vérifier votre dossier de spam. 
                      Si vous ne recevez toujours pas d'e-mail, 
                      cela signifie que vous n'avez pas de compte
                    </small>
                  </BaseMessage>
                </div>
              </div>
              <form
                v-else
                method="POST"
                action=""
                class="px-8 py-4"
                novalidate
                @submit.prevent="onSubmit"
              >
                <div class="mb-4 space-y-4">
                  <Field
                    v-slot="{ field, errorMessage, handleChange, handleBlur }"
                    name="email"
                  >
                    <BaseInput
                      :model-value="field.value"
                      :error="errorMessage"
                      :disabled="isSubmitting"
                      type="email"
                      label="Adresse email"
                      placeholder="Adresse email"
                      autocomplete="email"
                      :classes="{
                        input: 'h-12',
                      }"
                      @update:model-value="handleChange"
                      @blur="handleBlur"
                    />
                  </Field>
                </div>

                <div class="mb-6">
                  <BaseButton
                    :disabled="isSubmitting"
                    :loading="isSubmitting"
                    type="submit"
                    color="primary"
                    class="!h-12 w-full"
                  >
                  Réinitialiser le mot de passe
                  </BaseButton>
                </div>
                <!--No account link-->
                <p
                  class="text-muted-400 mt-4 flex justify-between font-sans text-sm leading-5"
                >
                  
                </p>
              </form>
            </Transition>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
