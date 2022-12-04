import {defineStore} from "pinia";
import {ref} from "vue";
import {useOptionService} from "@/services/option/optionService";
import type {Category} from "@/classes/category";

export const useOptionStore = defineStore("option", () => {
    const array: Category[] = [];
    const options = ref(array);
    const service = useOptionService();

    async function getOptions() {
        console.log("SEND REQUEST");

        const result = await service.getOption();
        // @ts-ignore
        options.value = result.data;
    }

    async function storeOptions(op: Category) {
        await service.storeOption(op.category);
        options.value.push(op);
    }

    return {
        getOptions: getOptions,
        storeOptions: storeOptions,
        options: options,
    };
});
