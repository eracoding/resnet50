import {defineStore} from "pinia";
import {ref} from "vue";
import {useOptionService} from "@/services/option/optionService";

export const useOptionStore = defineStore("option", () => {
    const array: string[] = [];
    const options = ref(array);
    const service = useOptionService();

    async function getOptions() {
        console.log("SEND REQUEST");

        const result = await service.getOption();
        // @ts-ignore
        options.value = result.data.map((e:object) => e.category);
        console.log(result.data);

    }

    async function storeOptions(op: string) {
        await service.storeOption(op);
        options.value.push(op);
    }

    return {
        getOptions: getOptions,
        storeOptions: storeOptions,
        options: options,
    };
});
