<script setup lang="ts">
import {useOptionStore} from "@/stores/option";
import {ref} from "vue";
import {storeToRefs} from "pinia";

const current = ref("");
let store = useOptionStore();
const {options} = storeToRefs(store);
store.getOptions();

function addOption() {
  store.storeOptions(current.value);
  current.value = "";
}
</script>

<template>
  <main>
    <div>
      <div :key="index" v-for="(value, index) in options">
        <span class="font-lg"> {{ value }}</span>
      </div>
      <input
          type="text"
          id="first_name"
          v-model="current"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="Category"
          required
      />
      <a href="#_"
         @click="addOption"
         class="relative mt-4 inline-flex items-center justify-center inline-block p-4 px-5 py-3 overflow-hidden font-medium text-indigo-600 rounded-lg shadow-2xl group">
        <span
            class="absolute top-0 left-0 w-40 h-40 -mt-10 -ml-3 transition-all duration-700 bg-red-500 rounded-full blur-md ease"></span><span
          class="absolute inset-0 w-full h-full transition duration-700 group-hover:rotate-180 ease">
        <span class="absolute bottom-0 left-0 w-24 h-24 -ml-10 bg-purple-500 rounded-full blur-md"></span>
        <span class="absolute bottom-0 right-0 w-24 h-24 -mr-10 bg-pink-500 rounded-full blur-md"></span>
        </span>
        <span class="relative text-white">Button Text</span>
      </a>


    </div>
  </main>
</template>
