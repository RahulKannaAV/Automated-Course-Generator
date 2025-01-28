"use client";
import {useState, useEffect} from "react";
import useAuth from "@/hooks/useAuth";
import { Typography } from "@mui/material";
import Cookies from "js-cookie";
import {Box} from "@mui/material";
import {ListItemText, List, ListItem} from "@mui/material";

const Recommendation = () => {
    const {currentUser} = useAuth();
    
    const userID = Cookies.get("userID");
    const [currentUserID, setCurrentUserID] = useState(userID);

    return (
        <Box
        component="main"
        >
            <div style={{display: "flex", flexDirection: "column"}}>
                <Typography variant="h2" style={{ textAlign: "center", marginLeft: "50px", marginTop: "100px"}}>
                    Based on your previous records
                </Typography>
                <Box sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper', justifyContent: "center", alignSelf: "center"}}>
                    <List>
                        {["Course 1", "Course 2"].map((course, idx) => (
                        <ListItem>
                            <ListItemText>
                                <Typography variant="h4" fontWeight="bolder">
                                    {course}
                                </Typography>
                            </ListItemText>
                        </ListItem>
                    ))}
                    </List>
                </Box>
            </div>
        </Box>
    )
}

export default Recommendation;