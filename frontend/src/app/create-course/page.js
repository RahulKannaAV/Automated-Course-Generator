"use client"
import styles from "./page.module.css";
import { TextField, Typography, Button } from "@mui/material";

const CourseCreation = () => {
    return (
        <div id={styles.page}>
            <div id={styles.course_form}>
                <div id={styles.message}>
                    <Typography variant="h3" sx={{
                        marginTop: "7%",
                        marginLeft: "10%"
                    }}>
                        ACP
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
                            fullWidth
                            placeholder="Enter Video URL"
                        />
                    </div>
                    <div className={styles.course_field}>
                        <Typography variant="h4">
                            Title
                        </Typography>
                        <TextField 
                            fullWidth
                            placeholder="Enter Course Title"
                        />
                    </div>
                    <div className={styles.course_submit}>
                        <Button variant="contained">Create Course</Button>

                    </div>
                </div>
            </div>
        </div>
    )
}

export default CourseCreation;