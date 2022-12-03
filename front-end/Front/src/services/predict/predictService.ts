import api from "@/services/api/api";

export const usePredictService = () => {
    async function predict(image: FormData) {
        return await api.post('api/predict',
            image, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                },

            }
        );
    }

    return {predict: predict}
}