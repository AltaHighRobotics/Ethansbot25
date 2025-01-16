/* Copyright (C) Cross The Road Electronics 2024 */
/**
 * WPI Compliant Pigeon class.
 * WPILIB's object model requires many interfaces to be implemented to use
 * the various features.
 * This includes...
 * - LiveWindow/Test mode features
 * - getRotation2d/Gyro Interface
 * - Simulation Hooks
 */

#pragma once

#include "ctre/phoenix/sensors/Pigeon2.h"
#include "ctre/phoenix/motorcontrol/can/TalonSRX.h"
#include "ctre/phoenix/WPI_CallbackHelper.h"

#include <mutex>

//Need to disable certain warnings for WPI headers.
#if __GNUC__
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#elif _MSC_VER
#pragma warning(push)
#pragma warning(disable : 4522 4458 4522)
#endif

#include "frc/geometry/Rotation2d.h"
#include "wpi/sendable/Sendable.h"
#include "wpi/sendable/SendableHelper.h"
#include "wpi/raw_ostream.h"
#include <hal/SimDevice.h>

//Put the warning settings back to normal
#if __GNUC__
#pragma GCC diagnostic pop
#elif _MSC_VER
#pragma warning(pop)
#endif

namespace ctre
{
namespace phoenix
{
namespace sensors
{

/**
 * Pigeon 2 Class. Class supports communicating over CANbus.
 *
 * @deprecated This device's Phoenix 5 API is deprecated for removal in the
 * 2025 season. Users should update to Phoenix 6 firmware and migrate to the
 * Phoenix 6 API. A migration guide is available at
 * https://v6.docs.ctr-electronics.com/en/stable/docs/migration/migration-guide/index.html.
 *
 * If the Phoenix 5 API must be used for this device, the device must have 22.X
 * firmware. This firmware is available in Tuner X after selecting Phoenix 5 in
 * the firmware year dropdown.
 */
class [[deprecated("This device's Phoenix 5 API is deprecated for removal in the 2025 season."
				"Users should update to Phoenix 6 firmware and migrate to the Phoenix 6 API."
				"A migration guide is available at https://v6.docs.ctr-electronics.com/en/stable/docs/migration/migration-guide/index.html")]]
WPI_Pigeon2 : public Pigeon2,
              public wpi::Sendable,
              public wpi::SendableHelper<WPI_Pigeon2>
{
  public:
    /**
     * Construtor for WPI_Pigeon2.
     *
     * @param deviceNumber CAN Device ID of the Pigeon 2.
     * @param canbus Name of the CANbus; can be a CANivore device name or serial number.
     *               Pass in nothing or "rio" to use the roboRIO.
     */
    WPI_Pigeon2(int deviceNumber, std::string const &canbus = "");

    ~WPI_Pigeon2();

    WPI_Pigeon2() = delete;
    WPI_Pigeon2(WPI_Pigeon2 const &) = delete;
    WPI_Pigeon2 &operator=(WPI_Pigeon2 const &) = delete;

    void InitSendable(wpi::SendableBuilder& builder) override;

    /**
     * \brief Resets the Pigeon 2 to a heading of zero.
     *
     * \details This can be used if there is significant drift in the gyro,
     * and it needs to be recalibrated after it has been running.
     */
    void Reset();
    /**
     * \brief Returns the heading of the robot in degrees.
     *
     * The angle increases as the Pigeon 2 turns clockwise when looked
     * at from the top. This follows the NED axis convention.
     *
     * \details The angle is continuous; that is, it will continue from
     * 360 to 361 degrees. This allows for algorithms that wouldn't want
     * to see a discontinuity in the gyro output as it sweeps past from
     * 360 to 0 on the second time around.
     *
     * \returns The current heading of the robot in degrees
     */
    double GetAngle() const;
    /**
     * \brief Returns the rate of rotation of the Pigeon 2.
     *
     * The rate is positive as the Pigeon 2 turns clockwise when looked
     * at from the top.
     *
     * \returns The current rate in degrees per second
     */
    double GetRate() const;
    /**
     * \brief Returns the heading of the robot as a frc#Rotation2d.
     *
     * The angle increases as the Pigeon 2 turns counterclockwise when
     * looked at from the top. This follows the NWU axis convention.
     *
     * \details The angle is continuous; that is, it will continue from
     * 360 to 361 degrees. This allows for algorithms that wouldn't want
     * to see a discontinuity in the gyro output as it sweeps past from
     * 360 to 0 on the second time around.
     *
     * \returns The current heading of the robot as a frc#Rotation2d
     */
    frc::Rotation2d GetRotation2d() const;

  private:
    void Init();

    DeviceType m_simType;

    hal::SimDevice m_simPigeon;
    hal::SimDouble m_simYaw;
    hal::SimDouble m_simRawYaw;

    static void OnValueChanged(const char* name, void* param, HAL_SimValueHandle handle,
                               HAL_Bool readonly, const struct HAL_Value* value);
    static void OnPeriodic(void* param);
};

} //namespace sensors
} //namespace phoenix
} //namespace ctre