import {
    BrowserRouter,
    Route,
    Routes,
} from "react-router-dom";
import SignIn from "./Screens/signInScreens/SignIn.jsx";
import HomeScreens from "./Screens/homeScreens/HomeScreens.jsx";
import ResponsiveAppBar from "./Components/ResponsiveAppBar.jsx";
import {CssBaseline, Container, Box} from "@mui/material";
import SettingsScreen from "./Screens/settingsScreens/settingsScreens.jsx";




function App() {
    return (
    <BrowserRouter>
            <CssBaseline>
                    <ResponsiveAppBar/>
{/* 
                    <Box  sx={{
                        backgroundColor: (theme) => theme.palette.grey[100]
                    }}> */}
                    <Box>
                        <Container maxWidth="xl">
                            <Routes>
                                <Route path="/" element={<HomeScreens />} exact/>
                                <Route path="/login" element={<SignIn />} exact/>
                                <Route path="/settings" element={<SettingsScreen />} exact/>
                            </Routes>
                        </Container>
                    </Box>
            
            </CssBaseline>
    </BrowserRouter>
  )
}

export default App
