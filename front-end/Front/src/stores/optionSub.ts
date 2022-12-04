import {defineStore} from "pinia";
import {computed, onUnmounted, ref} from "vue";
import {useOptionSubService} from "@/services/option/optionSubService";
import {useRoute} from "vue-router";
import type {Category} from "@/classes/category";

export const useOptionSubStore = defineStore("option-sub", () => {
    const array: Category[] = [];
    const options = ref(array);
    const service = useOptionSubService();
    const route = useRoute();
    const parent_id = computed(() => route.params.parent_id);

    async function getOptions() {
        console.log("SEND REQUEST");

        const result = await service.getOption(parent_id.value);
        options.value = result.data;
        console.log(result.data);

    }

    async function storeOptions(op: Category) {
        await service.storeOption(op.category, parent_id.value);
        options.value.push(op);
    }



    return {
        getOptions: getOptions,
        storeOptions: storeOptions,
        options: options,
    };
});
