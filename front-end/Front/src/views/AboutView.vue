<script>
import {computed, onMounted, ref} from 'vue'
import {usePredictService} from "../services/predict/predictService";


export default {
  // props seem best defined in the Object API style as we're used to
  props: {
    id: {type: String, default: 'drag-and-drop-input'},
    multiple: {type: Boolean, default: false},
    color: {type: String, default: 'gray'},
  },
  // Everything else goes in a setup function
  setup(props, {emit}) {
    const service = usePredictService();
    // keep up with the files state (think data)
    const files = ref([])

    // display the uploaded file names (think computed)
    const uploadInfo = computed(() => {
      return files.value.length === 1
          ? files.value[0].name
          : `${files.value.length} files selected`
    })

    // handle the file upload event (think methods)
    const handleUpload = (e) => {
      files.value = Array.from(e.target.files) || [];
    }

    function onDrop(e) {
      files.value = Array.from(e.dataTransfer.files) || []
      emit('input', [...e.dataTransfer.files])
    }

    function preventDefaults(e) {
      e.preventDefault()
    }

    const events = ['dragenter', 'dragover', 'dragleave', 'drop']

    async function predictResult() {
      const form = new FormData();
      form.append("image", files.value[0]);
      const result = await service.predict(form);
    }

    onMounted(() => {
      events.forEach((eventName) => {
        document.body.addEventListener(eventName, preventDefaults)
      })
    })
    return {files, uploadInfo, handleUpload, onDrop: onDrop, predictResult: predictResult}
  },
}
</script>
<template>
  <div @drop.prevent="onDrop" class="max-w-xl">
    <label
        class="flex justify-center w-full h-32 px-4 transition bg-white border-2 border-gray-300 border-dashed rounded-md appearance-none cursor-pointer hover:border-gray-400 focus:outline-none">
        <span class="flex items-center space-x-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-gray-600" fill="none" viewBox="0 0 24 24"
                 stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round"
                      d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"/>
            </svg>
           <small v-if="files.length" :class="`text-${color}-600 block`">
              <slot name="file" :files="files" :uploadInfo="uploadInfo">
                {{ uploadInfo }}
              </slot>
            </small>
            <span v-else class="font-medium text-gray-600">
                Drop files to Attach, or
                <span class="text-blue-600 underline">browse</span>
            </span>
        </span>
      <input @change="handleUpload"
             type="file" name="file_upload" class="hidden">
    </label>
    <a href="#_"
       @click="predictResult"
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
</template>

<style>
/* Finally we use Tailwind CSS to create our overlayed class */
.overlayed {
  @apply absolute top-0 left-0 right-0 bottom-0 w-full block;
}
</style>