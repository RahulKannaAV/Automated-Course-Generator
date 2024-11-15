"use client"
import CourseCard from "@/components/CourseCard";
import CourseTitleBar from "@/components/CourseTitleBar";
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid2';
import { styled } from '@mui/material/styles';
import { Typography } from "@mui/material";
import Link from "next/link";


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
    return (
        <div>
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
                    <Link href="/course/2">
                        <CourseCard 
                            gen_date={"02-05-2024"}
                            total_lectures={"10"}
                            completed_lectures={"5"}
                        />
                    </Link>
                        
                    
                </Grid>


            </Grid>
        </div>
    )
}

export default CourseDashboard;