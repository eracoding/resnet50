// @ts-ignore
import api from "../api/api";

export const useOptionService = () => {
    async function getOption() {
        return await api.get("api/category",);
    }

    async function storeOption(option: string) {
        return await api.post("api/category/create", {category: option});
    }

    return {
        storeOption: storeOption,
        getOption: getOption,
    };
};
