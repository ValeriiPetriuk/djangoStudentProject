import { Box, FormControl, InputLabel, Select, MenuItem } from "@mui/material";


export default function SelectDay({ day, handleChange }) {
    
    return (
      <Box sx={{ minWidth: 120}}>
        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">День</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={day}
            label="day"
            onChange={handleChange}
          >
            <MenuItem value="Понеділок">Понеділок</MenuItem>
            <MenuItem value="Вівторок">Вівторок</MenuItem>
            <MenuItem value="Середа">Середа</MenuItem>
            <MenuItem value="Четвер">Четвер</MenuItem>
            <MenuItem value="П'ятниця">Пятниця</MenuItem>
          </Select>
        </FormControl>
      </Box>
    );
  }