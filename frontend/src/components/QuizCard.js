"use client"
import { Button, Typography } from "@mui/material";
import {useState, useEffect} from "react";
import axios from "axios";
import useAuth from "@/hooks/useAuth";
import styles from "../app/quiz/[course_id]/page.module.css";


const QuizCard = (props) => {

    const { currentUserID } = useAuth();
    const options = ['Hyper Text ML', 'High Text Mark Low', 'Hyper Text Markup Language', 'How To Make Lasagna'];
    const [stats, setStats] = useState({
        "correct": 0,
        "wrong": 0
    });
    const [questions, setQuestions] = useState([]);
    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [chosen, setChosen] = useState(null);
    const [rightOption, setRightOption] = useState(0);
    const [isCorrect, setCorrectStatus] = useState();
    const [lockStatus, setLockStatus] = useState(false);

    useEffect(() => {
        const fetchQuestions = async() => {
            const response = await axios.get(`http://localhost:5000/fetch-questions?videoID=${props.videoID}&startTime=${props.startTime}&endTime=${props.endTime}&sectionID=${props.sectionID}&sectionName=${props.quizHeading}&courseName=${props.courseName}`);
            setQuestions(response.data);
        }

        fetchQuestions();
    }, [props.sectionID])

    console.log(questions);
    const handleChoiceSelection = (evt) => {
        setRightOption(questions[currentQuestion]["answer_option"])
        let buttonKey = evt.target.dataset.option;
        if(chosen == buttonKey) {
            setChosen(null);
        } else {
        setChosen(buttonKey)
        }
    }

    const showCorrectAnswer = () => {
        if(chosen == null) {
            console.log("Choose an option");
        } else {
            setLockStatus(true);
            console.log("Fetching Correct Answer");

            if(chosen == rightOption) {
                setCorrectStatus(true);
            } else {
                setCorrectStatus(false);
            }
        }
    }

    const bringNextQuestion = () => {
        setLockStatus(false);
        setChosen(null);
        setCurrentQuestion(currentQuestion+1);
        console.log("Next Question");
    }

    console.log(props.sectionID);
    return (
        questions.length == 0 ? 
        (
            <Typography variant="h4" style={{textAlign: "center"}}>
                Generating Quiz questions. Please Wait...
            </Typography>
        ) : currentQuestion < questions.length && (<div className={styles.quiz_card}>
                <div className={styles.quiz_header}>
                    <Typography 
                        variant="h4">
                        {props.quizHeading}
                    </Typography>
                    <Typography
                        variant="h4">
                        Time Left: 50s
                    </Typography>
                </div>
                <hr id={styles.partition}/>
                <div className={styles.quiz_question}>
                    <Typography
                        variant="h4"
                        style={{
                            marginTop: "15px",
                            marginBottom: "15px"
                        }}>
                        {currentQuestion + 1}) {questions[currentQuestion]["question_text"]}
                    </Typography>
                    {questions[currentQuestion]["options"].map((option, key) => (
                        <Button 
                            disabled={lockStatus}
                            key={key}
                            data-option={key}
                            color="warning"
                            className={styles.options}
                            onClick={handleChoiceSelection}
                            variant="outlined"
                            style={{
                                backgroundColor: (lockStatus ? ((chosen == key ? (isCorrect ? "green" : "red") : (key == rightOption && "green") )) : (chosen == key && "blue")) ,
                                display: "flex",
                                justifyContent: "flex-start",
                                margin: "15px",
                                fontSize: "17px"
                            }}>
                            {option}{lockStatus && (chosen == key ? (isCorrect ? "✅" : "❌") : (key == rightOption &&  "✅") )}
                        </Button>
                    ))}
                </div>
                <hr id={styles.partition}/>
                <div className={styles.quiz_stats}>
                    <Typography>
                        Question Number
                    </Typography>
                    {lockStatus ? 
                    (<Button
                        variant="contained"
                        onClick={bringNextQuestion}>
                        Next Question
                    </Button>) : (<Button
                        variant="contained"
                        onClick={showCorrectAnswer}>
                        Submit
                    </Button>)}
                    
                </div>
            </div>)
        
    )
}

export default QuizCard;