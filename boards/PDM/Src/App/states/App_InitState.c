#include "states/App_InitState.h"

#include "App_SharedMacros.h"

static void InitStateRunOnEntry(struct StateMachine *const state_machine)
{
    struct PdmWorld *world = App_SharedStateMachine_GetWorld(state_machine);
    struct PdmCanTxInterface *can_tx_interface = App_PdmWorld_GetCanTx(world);
    App_CanTx_SetPeriodicSignal_STATE(
        can_tx_interface, CANMSGS_PDM_STATE_MACHINE_STATE_INIT_CHOICE);
}

static void InitStateRunOnTick(struct StateMachine *const state_machine)
{
    UNUSED(state_machine);
}

static void InitStateRunOnExit(struct StateMachine *const state_machine)
{
    UNUSED(state_machine);
}

const struct State *App_GetInitState()
{
    static struct State init_state = {
        .name         = "INIT",
        .run_on_entry = InitStateRunOnEntry,
        .run_on_tick  = InitStateRunOnTick,
        .run_on_exit  = InitStateRunOnExit,
    };

    return &init_state;
}
