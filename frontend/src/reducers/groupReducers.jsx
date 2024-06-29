import { GROUPS_LIST_FAIL, GROUPS_LIST_REQUEST, GROUPS_LIST_SUCCESS } from "../constants/groupsConstans"

export const groupsListReducer = (state = {groups:[]}, action) => {
    switch (action.type) {
        case GROUPS_LIST_REQUEST:
            return {loading: true, groups:[], ...state}

        case GROUPS_LIST_SUCCESS:
            return {
                ...state,
                loading: false, 
                groups: action.payload
            }

        case GROUPS_LIST_FAIL:
            return {loading: false, error: action.payload}

        default: 
            return state
    }
}