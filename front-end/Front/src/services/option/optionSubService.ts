// @ts-ignore
import api from "../api/api";
import type {RouteParamValue} from "vue-router";

export const useOptionSubService = () => {
    async function getOption(parent_id: string | RouteParamValue[]) {
        return await api.get("api/category-sub?parent_id=" + parent_id.toString());
    }

    async function storeOption(option: string, parent_id: string | RouteParamValue[]) {
        return await api.post("api/category-sub/create", {
            category: option,
            parent: parent_id
        });
    }

    return {
        storeOption,
        getOption,
    };
};
