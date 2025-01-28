"use client";
import { Typography } from "@mui/material";
import axios from "axios";
import { useState, useEffect } from "react";


const ReferenceTab = (props) => {
    const [referenceData, setReferences] = useState([]);
    console.log(props);
    useEffect(() => {
        const getReferencesFromApi = async() => {
            const response = await axios.get(`http://localhost:5000/get-references?`+
             `heading=${props.heading}&`+
             `section_id=${props.sectionID}&`+
             `video_id=${props.videoID}&`+
             `start=${props.start}&`+
             `end=${props.end}`);

            setReferences(response.data);
        }

        if(props.videoID !== undefined && props.sectionID != undefined) {
        getReferencesFromApi();
        }
    }, [props.videoID, props.sectionID]);

    console.log(referenceData);

    return (
        <div>
            {referenceData.length === 0 && "Getting References..."}
            {referenceData.map((reference) => (
                <div>
                    <Typography variant="h4" fontWeight="bolder">
                        {reference.title}
                    </Typography>
                    <Typography variant="h5" color="red">
                        <a href={reference.URL} target="_blank">
                            {reference.URL}
                        </a>
                    </Typography>
                    <br />
                </div>
            ))}
        </div>
    )

}

export default ReferenceTab;

