"use client"
import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';

export default function CourseCard(props) {
  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardActionArea>
        <CardMedia
          component="img"
          height="140"
          image="/track-prog.png"
          alt="green iguana"
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            {props.course_name}
          </Typography>
          <Typography variant="body2" sx={{ color: 'text.secondary' }}>
            Course plan generated on <b>{props.gen_date}</b>
          </Typography>
          <Typography variant="body2" sx={{color: "text.secondary"}}>
              Progress done :  <b>{props.completed_lectures}</b> out of <b>{props.total_lectures}</b> lectures
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}
