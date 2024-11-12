'use client'
import { useState, useEffect } from "react";
import axios from "axios";

function Test() {
    const [text, setText] = useState("Next JS")
    useEffect(() => {
        async function getFromApi() {
            try {
                const response = await axios.get("http://localhost:5000/hello");
                setText(response.data);
            } catch(e) {
                console.error("Error in obtaining data:", e);
            }
        }

        async function postToApi() {
            try {
                const postRequest = await axios.post("http://localhost:5000/data", {
                    name: "Shankar",
                    age:23
                });
                console.log("Data sent successfully");
                console.log("Data received from request: ", postRequest.data);
            } catch(e) {
                console.error("Error in sending data", e);
            }
        }

        getFromApi();
        postToApi();
    }, []);
    return <h1>Hello World from {text}</h1>
}

export default Test;