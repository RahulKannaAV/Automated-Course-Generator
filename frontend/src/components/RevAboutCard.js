import styles from "../app/page.module.css";
import Image from "next/image";
import { Typography } from "@mui/material";

const RevAboutCard = (props) => {
    return (
        <div className={styles.course_card}>
        <Typography 
          variant="h4"
          sx={{
            width: "40%",
            textAlign:"center",
            marginTop: "7%"
          }} >
            {props.textContent}
        </Typography>
        <Image 
          src={props.src}
          width={props.width || 450}
          height={props.height ||300}
          />
      </div>
    );
}

export default RevAboutCard;