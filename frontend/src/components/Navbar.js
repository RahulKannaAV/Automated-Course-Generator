"use client";
import { Button, AppBar, Toolbar, Typography, Box } from "@mui/material";
import Cookies from "js-cookie";
import { useState, useEffect } from "react";
import Link from "next/link";

const Navbar = () => {
    const [loggedIn, setLoggedIn] = useState(false);
    const [userID, setUserID] = useState("");
    const [properties, setProperties] = useState({});

    const startLogin = async() => {
      window.location.href = "http://localhost:5000/google-login";
    }

    const logoutClient = async() => {
      window.location.href = "http://localhost:5000/logout";
    }

    const createCourse = async() => {
      window.location.href = "http://localhost:3000/create-course";
    }

    useEffect(() => {
      const checkAuthStatus = () => {
        let cookieUserID = Cookies.get("userID");
        console.log(cookieUserID);
        if(cookieUserID !== undefined) {
          setLoggedIn(true);
          setUserID(cookieUserID);
        } else {
          setLoggedIn(false);
        }

        setProperties({
          buttonColor: loggedIn ? "red" : "inherit",
          buttonText: loggedIn ? `User ${userID}` : "Login",
          textColor: loggedIn ? "red" : "black",
          executeFunction: loggedIn ?  logoutClient : startLogin
    
        });
      };

      checkAuthStatus();
    }, [loggedIn]);


    
    return (
    <Box sx={{ flexGrow: 1,
     }}>
      <AppBar position="static"
      sx={{
        backgroundColor: "darkblue",
        marginBottom: "25px"
      }}>
        <Toolbar>
          <Typography variant="h4" component="div" sx={{ flexGrow: 1 }}>
            ACG
          </Typography>
          <Button onClick={properties.executeFunction} style={{backgroundColor: properties. buttonColor}} color={properties.textColor}>{properties.buttonText}</Button>
          <Link href="/create-course">
            <Button color="inherit">Create</Button>
          </Link>          
          <Button color="inherit">About</Button>
          <Button color="inherit">How To</Button>
        </Toolbar>
      </AppBar>
    </Box>
    )
}

export default Navbar;