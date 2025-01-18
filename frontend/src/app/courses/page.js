"use client"
import CourseCard from "@/components/CourseCard";
import CourseTitleBar from "@/components/CourseTitleBar";
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid2';
import {useState, useEffect} from "react";
import { styled } from '@mui/material/styles';
import styles from "./page.module.css";
import { Typography } from "@mui/material";
import Link from "next/link";
import Cookies from "js-cookie";
import axios from "axios";
import { useRouter } from "next/navigation";
import useAuth from "@/hooks/useAuth";


const Item = styled(Paper)(({ theme }) => ({
    backgroundColor: '#fff',
    ...theme.typography.body2,
    padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary,
    ...theme.applyStyles('dark', {
      backgroundColor: 'orange',
    }),
  }));

  const CourseDashboard = () => {
    const [courses, setCourses] = useState([]);
    const {currentUserID} = useAuth();

    console.log(currentUserID);


    useEffect(() => {
        const getAllCourseMetadata = async() => {
            const coursesJson = await axios.get("http://localhost:5000/get-courses");
            setCourses(coursesJson.data);
        }

        getAllCourseMetadata();
    }, [])


    return (
        <div className={styles.course_dashboard}>
            <CourseTitleBar title={"AUTOMATED COURSE GENERATOR"} />
            <Typography
                variant="h4"
                sx={{
                    fontWeight: "bold",
                    fontSize: 42,
                    margin: "50px" 
                }}>
                Available Courses
            </Typography>
            <Grid container spacing={2} sx={{
                marginLeft: "50px",
                marginTop: "50px",
                paddingBottom: "50px",
            }}>
                <Grid size={{sm: 12, md: 6, lg: 4, xl: 3}} sx={{
                    boxShadow: "none"
                }}
                >
                    {courses.map((course, key) => (
                        <Link href={`/course/${course.course_id}`}>
                            <CourseCard 
                                course_name={course.course_name}
                                gen_date={course.generated_date}
                                total_lectures={"10"}
                                completed_lectures={"5"}
                            />
                        </Link>
                    ))}

                        
                    
                </Grid>


            </Grid>
        </div>
    )
}

export default CourseDashboard;