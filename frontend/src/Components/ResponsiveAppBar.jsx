import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import {useState} from "react";
import {Drawer, List, ListItem, ListItemButton, ListItemIcon, ListItemText, Hidden, Link} from "@mui/material";
import SettingsIcon from '@mui/icons-material/Settings';
import LoginIcon from '@mui/icons-material/Login';
import { Link as RouterLink} from 'react-router-dom';

const ResponsiveAppBar = () => {
    const [isDrawerOpen, setDrawerOpen] = useState(false);

    const DrawerList = (
    <Box sx={{ width: 250 }} role="presentation" onClick={() => setDrawerOpen(false)}>
      <List>
        <RouterLink to='/settings'>  
            <ListItem  disablePadding>
              <ListItemButton>
                <ListItemIcon>
                  <SettingsIcon/>
                </ListItemIcon>
                <ListItemText primary="Settings" />
              </ListItemButton>
            </ListItem>
          </RouterLink>

        <RouterLink to='/login'>  
          <ListItem  disablePadding>
            <ListItemButton>
              <ListItemIcon>
                <LoginIcon/>
              </ListItemIcon>
              <ListItemText primary="Login" />
            </ListItemButton>
          </ListItem>
          </RouterLink>
      </List>
      
    
    
    </Box>
  );

     return (
        <Box>
            <AppBar position="static">
                <Toolbar>
                    <Hidden only={['lg', 'xl']}>
                      <IconButton onClick={() => setDrawerOpen(true)}
                        size="large"
                        edge="start"
                        color="inherit"
                        aria-label="menu"
                        sx={{ mr: 2 }}
                      >
                        <MenuIcon />

                      </IconButton>
                    </Hidden>
                    <Link component={RouterLink} to='/' sx={{flexGrow: 1}}>
                      <Typography variant="h6" component="div" sx={{color:'white', flexGrow: 1 }}>
                          Student
                        </Typography>
                    </Link>
                 
                      
                      {/* <Box sx={{ flexGrow: 1}}>
                        <Button
                          sx={{ my: 2, color: 'white', display: 'block' }}
                        >
                          Settings
                        </Button>
                    </Box> */}
                    <Link component={RouterLink} to='/settings'>  
                      <Button  sx={{ my: 2, color: 'white', display: 'block' }} color="inherit">Settings</Button>
                    </Link>
                    <Link component={RouterLink} to='/login'>  
                      <Button  sx={{ my: 2, color: 'white', display: 'block' }} color="inherit">Login</Button>
                    </Link>
                </Toolbar>
            </AppBar>
            <Drawer
                anchor="left"
                open={isDrawerOpen}
                onClose={() => setDrawerOpen(false)}>
                {DrawerList}
            </Drawer>
        </Box>
  );
}
export default ResponsiveAppBar;
