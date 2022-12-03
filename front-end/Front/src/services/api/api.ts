import axios from "axios";

const SERVER = "http://127.0.0.1:8000/";
const instance = axios.create({
    baseURL: SERVER + "/",
    headers: {
        // "Access-Control-Allow-Headers" : 'Origin,Content-Type,X-Requested-With,Accept,Authorization, Access-Control-Allow-Methods',
        // 'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, PUT, PATCH, DELETE',
        // 'Access-Control-Allow-Origin': "*",
        // "Content-Type": "application/json, text/plain, */*",
        // Accept: "application/json",
    },
});
export default instance;
