import Modal from '@mui/joy/Modal';
import { Typography } from '@mui/material';
import { useState } from 'react';
import CircularProgress from '@mui/material/CircularProgress';
import Sheet from '@mui/joy/Sheet';
import {Box} from '@mui/material';


export default function LoadingModal(props) {
    const [message, setMessage] = useState(props.message);
    const [description, setDescription] = useState(props.desc);

    return (
        <Modal
        key={props.key}
        aria-labelledby="modal-title"
        aria-describedby="modal-desc"
        open={open}
        sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}
      >
        <Sheet
          variant="outlined"
          sx={{ maxWidth: 500, borderRadius: 'md', p: 3, boxShadow: 'lg' }}
        >
          <Typography
            variant="h2"
            id="modal-title"
            level="h4"
            textColor="inherit"
            sx={{textAlign: "center",
              paddingBottom: "40px"
            }}
          >
            {message}
          </Typography>
          <Typography 
            id="modal-desc" textColor="text.tertiary"
            sx={{fontSize: 22,
              textAlign: "center",
              paddingBottom: "40px"
            }}>
              {description}
          </Typography>
          <Box sx={{
            display: "flex",
            justifyContent: "center",
            paddingBottom: "30px"
          }}>
            <CircularProgress 
            size={50}
            sx={{
              alignContent: "center",
            }} />
          </Box>
        </Sheet>
      </Modal>
    )
}
