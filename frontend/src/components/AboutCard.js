import styles from "../app/page.module.css";
import Image from "next/image";
import { Typography } from "@mui/material";

const AboutCard = (props) => {
    return (
        <div className={styles.course_card}>
        <Image 
          src={props.src}
          width={ props.width || 450}
          height={300}
          />
        <Typography 
          variant="h4"
          sx={{
            width: "40%",
            textAlign:"center",
            marginTop: "7%"
          }} >
            {props.textContent}
        </Typography>
      </div>
    );
}

export default AboutCard;