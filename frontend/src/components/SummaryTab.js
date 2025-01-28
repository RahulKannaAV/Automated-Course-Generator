"use client"
import { useState, useEffect } from "react";
import { Typography } from "@mui/material";
import axios from "axios";

const SummaryTab = (props) => {
    const [summary, setSummary] = useState({});

    useEffect(() => {
        const getSummaryText = async() => {
            try {
            const summaryResponse = await axios.get(`http://localhost:5000/generate-summary?heading=${props.heading}&section_id=${props.sectionID}&video_id=${props.videoID}&start=${props.startTime}&end=${props.endTime}`);
            setSummary(summaryResponse.data);
            } catch(e) {
              console.error(`Error in fetching summary text: ${e}`);
            }
            
          }
        console.log("Heyyo ");
        getSummaryText();
    }, [])




    console.log(summary);
    return (
        <div>
            {Object.keys(summary).length == 0 && "Generating it..."  }

            <Typography variant="h3">
                {summary.title}
            </Typography>

            <br />
            <br />


            { summary.sections !== undefined &&
            summary.sections.map((section) => {
                return (
                <div>
                    <Typography variant="h4">
                    &emsp;{section.title}
                    </Typography>
                    <br />

                    {section.topics.map((topic) => {
                        return (
                            <div>
                                {topic.name.length > 0 && <Typography variant="h5" fontWeight="bolder">
                                    &emsp;&emsp;{topic.name}
                                </Typography>}
                                

                                {topic.description.length > 0 && <Typography variant="h6">
                                    &emsp;&emsp;&emsp;{topic.description}
                                </Typography>}

                                {topic.example !== undefined && (<Typography variant="h6" fontWeight="bolder">
                                    &emsp;&emsp;&emsp; Example: {topic.example}
                                </Typography>)}

                                <br />
                            </div>
                        )
                    })}

                </div>
                )
            })
            }
        </div>
    );
}

export default SummaryTab;