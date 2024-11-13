import Navbar from "@/components/Navbar";
import styles from "./page.module.css"
import Image from "next/image";
import { Typography } from "@mui/material";
import AboutCard from "@/components/AboutCard";
import RevAboutCard from "@/components/RevAboutCard";

const LandingPage = () => {
  console.log(styles);
  return (
    <div className={styles.bg}>
      <Navbar />
      <div className={styles.image_container}>
        <Typography
          variant="h1"
          color="white"
          sx={{
            paddingBottom: "40px",
            fontFamily: "Inter, sans-serif",
            width: "60%",
            textAlign: "center",
            fontWeight: 500
          }}
          >
            Automated Course Planner
        </Typography>
        <Typography
          variant="h4"
          sx={{
            color: "white",
            fontFamily: "Verdana",
            fontSize: 25,
            textAlign: "center",
            width: "40%",
            paddingBottom: "40px"
}}>
            Utility tool to create your own Course Plan. Have a Structured Learning
        </Typography>
        <Image 
          src={"/land-pic.png"} 
          width={450}
          height={300}
          />
      </div>
      <div style={{
        padding: "50px 0",
        backgroundColor: "gray"
      }}>
      <AboutCard 
        src={"/pers-learn.png"}
        textContent={"Personal Learning made easy"}
        width={700}
      />

      <RevAboutCard 
        src={"/track-prog.png"}
        textContent={"Track your Learning progress to improve further"}
      />

      <AboutCard 
        src={"/summaries.jpeg"}
        textContent={"Get summaries of your learning content to revise quicker"}
      />
      </div>
      
    </div>
  )
}

export default LandingPage;