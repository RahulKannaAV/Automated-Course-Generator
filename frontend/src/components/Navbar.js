import { Button, AppBar, Toolbar, Typography, Box } from "@mui/material";

const Navbar = () => {
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
            ACP
          </Typography>
          <Button color="inherit">Login</Button>
          <Button color="inherit">Create</Button>
          <Button color="inherit">About</Button>
          <Button color="inherit">How To</Button>
        </Toolbar>
      </AppBar>
    </Box>
    )
}

export default Navbar;