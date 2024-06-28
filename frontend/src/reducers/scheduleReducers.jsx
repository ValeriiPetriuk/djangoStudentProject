import { SCHEDULE_LIST_FAIL, SCHEDULE_LIST_REQUEST, SCHEDULE_LIST_SUCCESS } from "../constants/scheduleConstans"



export const scheduleListReducer = (state = {schedule:[]}, action) => {
    switch (action.type) {
        case SCHEDULE_LIST_REQUEST:
            return {loading: true, schedule:[], ...state}

        case SCHEDULE_LIST_SUCCESS:
            return {
                ...state,
                loading: false, 
                schedule: action.payload
            }

        case SCHEDULE_LIST_FAIL:
            return {loading: false, error: action.payload}

        default: 
            return state
    }
}