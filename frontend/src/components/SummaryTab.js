"use client"
import { useState, useEffect } from "react";
import { Typography } from "@mui/material";

const SummaryTab = ({data}) => {
    console.log(data.sections);
    return (
        <div>

            <Typography variant="h3">
                {data.title}
            </Typography>

            <br />
            <br />


            {
            data.sections.map((section) => {
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

                                {topic.example.length > 0 && <Typography variant="h6" fontWeight="bolder">
                                    &emsp;&emsp;&emsp; Example: {topic.example}
                                </Typography>}

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