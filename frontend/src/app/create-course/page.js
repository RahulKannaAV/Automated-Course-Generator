"use client"
import { useState, useEffect } from "react";
import styles from "./page.module.css";
import axios from 'axios';
import {useRouter} from "next/navigation";
import LoadingModal from "@/components/Modal";
import { TextField, Typography, Button } from "@mui/material";
import useAuth from "@/hooks/useAuth";
import Link from "next/link";
import Cookies from "js-cookie";

const CourseCreation = () => {
    const router = useRouter();
    const { currentUserID } = useAuth();



    const [openModal, setModal] = useState(false);
    const [courseData, setCourseData] = useState({
        "course_name": "",
        "course_url": "",
        "userID": Cookies.get("userID")
    });



    const [status, setStatus] = useState("Sit back and relax. We got this for you.");
    useEffect(() => {
        // Create EventSource instance for listening to events
        const eventSource = new EventSource('http://localhost:5000/events');
        
        console.log(eventSource);
        // EventSource on message handler
        eventSource.onmessage = (event) => {
          const parsedData = JSON.parse(event.data);
          console.log("Received event:", parsedData.data);  // Log to track event sequence
          setStatus(parsedData.data);  // Update status based on event data
        };
    
        // EventSource error handler
        eventSource.onerror = () => {
          console.error("EventSource connection error.");
          eventSource.close();
        };
    
        // Reconnect on close or error
        eventSource.onclose = () => {
          console.log("EventSource connection closed. Reconnecting...");
          setTimeout(() => {
            const eventSource = new EventSource('http://localhost:5000/events');
          }, 5000); // Retry every 5 seconds
        };
    
        // Cleanup: Close the connection when the component unmounts
        return () => {
          eventSource.close();
        };
      }, [courseData]);

    const handleStartTask = async () => {        
        try {

            setModal(!openModal);
            
            // Start the task on the server
            const sendResult = await axios.post("http://localhost:5000/new-course", courseData);
            console.log(sendResult);
            // Begin listening for events if not already listening
            setModal(false);

            router.push("/courses");
            
            
        } catch (error) {
            console.error("Error starting task:", error);
            setStatus("Failed to start task.");
        }
    };

    const handleCourseTitle = (evt) => {
        setCourseData({...courseData, "course_name": evt.target.value});
    }

    const handleCourseURL = (evt) => {
        setCourseData({...courseData, "course_url": evt.target.value});
    }

    return (
        <div id={styles.page}>
            {openModal && <LoadingModal 
                            key={status}
                            message={"Preparing the plan"} 
                            desc={status}  />}
            <div id={styles.course_form}>
                <div id={styles.message}>
                    <Typography variant="h3" sx={{
                        marginTop: "7%",
                        marginLeft: "10%"
                    }}>
                        <Link href="/">
                            ACG
                        </Link>
                    </Typography>
                    <div id={styles.text}>
                        <Typography variant="h2" sx={{
                            marginBottom: "20px"
                        }}>
                            Learn for the Future
                        </Typography>
                        <Typography variant="h5">
                            Create course plans with no hassle
                        </Typography>
                    </div>
                </div>
                <div id={styles.course_input}>
                    <Typography variant="h3" sx={{
                        textAlign: "center",
                        marginTop: "5%"
                    }}>
                        Create a Course
                    </Typography>
                    <div className={styles.course_field}>
                        <Typography variant="h4">
                            Video URL
                        </Typography>
                        <TextField 
                            onChange={handleCourseURL}
                            fullWidth
                            placeholder="Enter Video URL"
                        />
                    </div>
                    <div className={styles.course_field}>
                        <Typography variant="h4">
                            Title
                        </Typography>
                        <TextField 
                            onChange={handleCourseTitle}
                            fullWidth
                            placeholder="Enter Course Title"
                        />
                    </div>
                    <div className={styles.course_submit}>
                        <Button variant="contained" onClick={handleStartTask}>
                            Create Course
                        </Button>

                    </div>
                </div>
            </div>
        </div>
    )
}

export default CourseCreation;