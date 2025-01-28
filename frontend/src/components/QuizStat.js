"use client"
import { Button, Typography } from "@mui/material";
import {useState, useEffect} from "react";
import axios from "axios";
import styles from "../app/quiz/[course_id]/page.module.css";
import { useRouter } from "next/navigation";


const QuizStats = (props) => {

    const router = useRouter();
    const goToHomePage = () => {
        window.location.reload()
    }

    return (
            <div className={styles.quiz_card}>
                <div className={styles.quiz_header}>
                    <Typography
                        variant="h4">
                        {props.quizTitle}
                    </Typography>
                </div>
                <hr id={styles.partition}/>
                <Typography
                            variant="h3"
                            style={{
                                textAlign: "center",
                                marginTop: "10%",
                                marginBottom: "15px",
                                color: "blue",
                                backgroundColor: "white"
                                }}>
                            Attempted : {props.stats.attempted}/{props.stats.total} question{props.stats.attempted > 1 && "s"}
                    </Typography>
                    <Typography
                            variant="h3"
                            style={{
                                textAlign: "center",
                                marginTop: "15px",
                                marginBottom: "15px",
                                color: "green"
                                }}>
                            Correct : {props.stats.correct}/{props.stats.total} question{props.stats.correct > 1 && "s"}
                    </Typography>
                    <Typography
                        variant="h3"
                        style={{
                            textAlign: "center",
                             marginTop: "15px",
                            marginBottom: "10%",
                            color: "red"
                        }}>
                            Incorrect: {props.stats.wrong}/{props.stats.total} question{props.stats.wrong > 1 && "s"}
                    </Typography>
                <div className={styles.quiz_stats}>
                    <Button
                        variant="contained"
                        onClick={goToHomePage}>
                        Go to Home
                    </Button>
                </div>
            </div>
    )
}

export default QuizStats;