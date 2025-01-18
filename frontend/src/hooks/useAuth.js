import Cookies from "js-cookie";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";


const useAuth = () => {
    const [currentUserID, setCurrentUserID] = useState("");
    const router = useRouter();

    useEffect(() => {
        const checkAuth = async() => {
            const userID = Cookies.get("userID");
            console.log(userID);
            if(userID === undefined) {
                router.push("/");
            } else {
                setCurrentUserID(currentUserID);
            }
        }
        
        const interval = setInterval(checkAuth, 1000);

        return () => clearInterval(interval);
    }, [])

    return {currentUserID}
}

export default useAuth;