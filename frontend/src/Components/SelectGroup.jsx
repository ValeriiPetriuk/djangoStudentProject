import { Box, FormControl, InputLabel, Select, MenuItem, CircularProgress } from "@mui/material";


export default function SelectGroup({group, handleChangeGroup, groups}) {
  
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
          {groups.map(item => (
            <MenuItem value={item.name} key={item.id}>{item.name}</MenuItem>
          ))}
          </Select>
        </FormControl>
      </Box>
    );
  }