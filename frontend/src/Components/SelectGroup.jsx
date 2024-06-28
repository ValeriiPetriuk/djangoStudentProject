import { Box, FormControl, InputLabel, Select, MenuItem } from "@mui/material";


export default function SelectGroup({group, handleChangeGroup}) {
   
  
    return (
      <Box sx={{ minWidth: 120 }}>
        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">Група</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={group}
            label="day"
            onChange={handleChangeGroup}
          >
            <MenuItem value="PS3-1">ПС3-1</MenuItem>
            <MenuItem value="PS1-1">ПС1-1</MenuItem>
    
          </Select>
        </FormControl>
      </Box>
    );
  }