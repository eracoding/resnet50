<script setup lang="ts">
import {onUnmounted, ref} from "vue";
import {storeToRefs} from "pinia";
import {useOptionSubStore} from "@/stores/optionSub";
import type {Category} from "@/classes/category";

const current = ref("");
let store = useOptionSubStore();
const {options} = storeToRefs(store);
store.getOptions();
onUnmounted(() => {
  console.log("deleted");
  options.value = [];
})

function addOption() {
  const modal = {
    id: 0,
    category: current.value,
  } as Category;
  store.storeOptions(modal);
  current.value = "";
}
</script>

<template>
  <main class="">
    <h1 class="green" style="font-size: 30px"> {{ $route.params.category }}</h1>
    <div>
      <div class="h-[50vh] overflow-scroll pr-4">
        <div class="flex  p-2 flex-row justify-between border-radius-lg " :key="index"
             v-for="(value, index) in options">
          <span class="font-lg "> {{ value.category }}</span>
        </div>
      </div>
      <input
          type="text"
          id="first_name"
          v-model="current"
          class=" mt-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="Category"
          required
      />
      <a href=""
         @click="addOption"
         class="relative mt-4 inline-flex items-center justify-center inline-block p-4 px-5 py-3 overflow-hidden font-medium text-indigo-600 rounded-lg shadow-2xl group">
        <span
            class="absolute top-0 left-0 w-40 h-40 -mt-10 -ml-3 transition-all duration-700 bg-red-500 rounded-full blur-md ease"></span><span
          class="absolute inset-0 w-full h-full transition duration-700 group-hover:rotate-180 ease">
        <span class="absolute bottom-0 left-0 w-24 h-24 -ml-10 bg-purple-500 rounded-full blur-md"></span>
        <span class="absolute bottom-0 right-0 w-24 h-24 -mr-10 bg-pink-500 rounded-full blur-md"></span>
        </span>
        <span class="relative text-white">Добавить</span>
      </a>
    </div>
  </main>
</template>