# -*- coding: utf-8 -*-
"""
.. module:: simple.py
   :platform: Unix
   :synopsis: Generate test files in data exchange.

:Author:
  `Francesco De Carlo <mailto: decarlof@gmail.com>`_

:Organization:
  Argonne National Laboratory, Argonne, IL 60439 USA

:Version: 2014.08.15
"""

import os
import timeimport pytzimport datetimeimport numpy as np
import dxfile.dxtomo as dx

def iso_time():
    # set the experiment date     now = datetime.datetime.today()

    # set iso format time    central = pytz.timezone('US/Central')    local_time = central.localize(now)    local_time_iso = local_time.isoformat()
    
    return local_time_iso

def main():

    fname = './demo.h5'
    ccd_x, ccd_y = 128, 128
    
    sample_name = 'sample_name'
    sample_description = 'sample description' 
    sample_preparation_date = iso_time()
    sample_chemical_formula = 'H2O'   
    sample_mass = '1234'
    sample_concentration  = '1234'  
    sample_environment = '1234'
    sample_temperature = '1234'
    sample_temperature_set = '1234'
    sample_pressure = '1234'
    sample_thickness = '1234'
    sample_tray = 'A5'
    sample_comment = 'sample comment'

    experiment_prosal = '1234'
    experiment_activity = '5678'
    experiment_safety = '9012'

    experimenter_name = 'Joe'
    experimenter_role = 'PI'
    experimenter_affiliation = 'Argonne National Laboratory'
    experimenter_address = '9700 S. Cass Av.'
    experimenter_phone = '1-123-456-7890'
    experimenter_email = 'joe@aps.anl.gov'
    experimenter_facility_user_id = '1234'

    instrument_name = '32-ID TXM'  
    instrument_comment = 'nice instrument'  

    source_name = 'APS'
    source_datetime = iso_time()
    source_beamline = 'U18'
    source_current = '100'
    source_energy = '123'
    source_pulse_energy = '45'
    source_pulse_width = '67'
    source_mode = 'top-up'
    source_beam_intensity_incident = '123'
    source_beam_intensity_transmitted = '456'
    
    attenuator_name = 'filter'
    attenuator_description = 'a nice filter'
    attenuator_thickness = '123'
    attenuator_transmission = '456'
    
    monochromator_name = 'mono'
    monochromator_description = 'a nice mono'
    monochromator_energy = '123'
    monochromator_energy_error = '456'
    monochromator_mono_stripe = 'Au/Ag'
            
    mirror_name = 'mirror'
    mirror_description = 'a nice mirror'

    detector_name = 'camera'
    detector_description = 'a nice camera'
    detector_manufacturer = 'a nice company'
    detector_model = '123'
    detector_serial_number = '456'
    detector_firmware_version = '789'
    detector_software_version = '012'
    detector_bit_dept = '16'
    detector_pixel_size_x = '6.5'
    detector_pixel_size_y = '6.5'
    detector_actual_pixel_size_x = '1.2'
    detector_actual_pixel_size_y = '1.2'
    detector_dimension_x = ccd_x
    detector_dimension_y = ccd_y
    detector_binning_x = '1'
    detector_binning_y = '1'
    detector_operating_temperature = '12'
    detector_exposure_time = 0.2
    detector_delay_time = 0.001
    detector_stabilization_time = 0.0001
    detector_frame_rate = 160
    detector_output_data = '/exchange'
    detector_counts_per_joule = '123'
    detector_basis_vectors = '456'
    detector_corner_position = '789'

    detector_roi_name = 'roi'
    detector_roi_description = 'a nice roi'
    detector_roi_min_x = 0
    detector_roi_min_y = 0
    detector_roi_size_x = ccd_x
    detector_roi_size_y = ccd_y

    objective_name = 'objective'
    objective_description = 'a nice objective'
    objective_manufacturer = 'a nice company'
    objective_model = 'a nice model'
    objective_magnification = 1.5
    objective_numerical_aperture = 0.8

    scintillator_name = 'scintillator' 
    scintillator_description = 'a nice scintillator' 
    scintillator_manufacturer = 'a nice company' 
    scintillator_serial_number = '123'
    scintillator_scintillating_thickness = '456'
    scintillator_substrate_thickness = '789'

    sample_stack_name = 'sample stack'
    sample_stack_description = 'a nice sample stack'

    sample_stack_setup_sample_x = 1
    sample_stack_setup_sample_y = 2
    sample_stack_setup_sample_z = 3
    sample_stack_setup_sample_xx = 11
    sample_stack_setup_sample_zz = 33

    interferometer_name = 'interferometer'
    interferometer_description = 'a nice interferometer'

    interferometer_setup_grid_start = 123
    interferometer_setup_grid_end = 456
    interferometer_setup_number_of_grid_periods = 789
    interferometer_setup_number_of_grid_steps = 123


    process_name = 'the best process'

    acquisition_sample_position_x = np.random.rand(180)
    acquisition_sample_position_y = np.random.rand(180)
    acquisition_sample_position_z = np.random.rand(180)
    acquisition_sample_image_shift_x = np.random.rand(180)
    acquisition_sample_image_shift_y = np.random.rand(180)
    acquisition_image_theta = range(0, 180, 1)
    acquisition_scan_index = range(0, 180, 1)
    acquisition_scan_date = [iso_time() for x in range(180)]
    acquisition_image_date = [iso_time() for x in range(180)]
    acquisition_time_stamp = [iso_time() for x in range(180)]
    acquisition_image_number = range(0, 180, 1)
    acquisition_image_exposure_time = np.ones(180) * detector_exposure_time
    acquisition_image_is_complete = np.ones(180)
    acquisition_shutter = np.ones(180)
    acquisition_image_type = np.ones(180)
    acquisition_start_date = iso_time()
    acquisition_end_date = iso_time()

    acquisition_setup_number_of_projections = 180
    acquisition_setup_number_of_darks = 10
    acquisition_setup_number_of_whites = 10
    acquisition_setup_number_of_inter_whites = 1
    acquisition_setup_white_frequency = 1
    acquisition_setup_sample_in = 0
    acquisition_setup_sample_out = 4
    acquisition_setup_rotation_start_angle = 0
    acquisition_setup_rotation_end_angle = 180
    acquisition_setup_angular_step = (acquisition_setup_rotation_end_angle - acquisition_setup_rotation_start_angle) / 180
    acquisition_setup_mode = 'fly scan'
    acquisition_setup_comment = 'a nice fly scan'


    data = np.random.rand(180, ccd_y, ccd_x)
    data_white = np.ones((acquisition_setup_number_of_whites, ccd_y, ccd_x)) # Array filled with zeros
    data_dark = np.zeros((acquisition_setup_number_of_darks, ccd_y, ccd_x)) # Array filled with zeros
    theta = range(0, 180, 1)


    if (fname != None):
        if os.path.isfile(fname):
            print "Data Exchange file already exists: ", fname
        else:
            # Create new folder.
            dirPath = os.path.dirname(fname)
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)

            # Open DataExchange file
            f = dx.File(fname, mode='w') 

            # Write the Data Exchange HDF5 file.
            f.add_entry(dx.Entry.sample( name={'value':sample_name}))
            f.add_entry(dx.Entry.sample( description={'value':sample_description}))    
            f.add_entry(dx.Entry.sample( preparation_date={'value':sample_preparation_date}))   
            f.add_entry(dx.Entry.sample( chemical_formula={'value':sample_chemical_formula}))    
            f.add_entry(dx.Entry.sample( mass={'value':sample_mass}))    
            f.add_entry(dx.Entry.sample( concentration={'value':sample_concentration}))    
            f.add_entry(dx.Entry.sample( environment={'value':sample_environment}))
            f.add_entry(dx.Entry.sample( temperature={'value':sample_temperature}))
            f.add_entry(dx.Entry.sample( temperature_set={'value':sample_temperature_set}))
            f.add_entry(dx.Entry.sample( pressure={'value':sample_pressure}))
            f.add_entry(dx.Entry.sample( thickness={'value':sample_thickness}))
            f.add_entry(dx.Entry.sample( tray={'value':sample_tray}))
            f.add_entry(dx.Entry.sample( comment={'value':sample_comment}))
            
            f.add_entry(dx.Entry.experiment( proposal={'value':experiment_prosal}))
            f.add_entry(dx.Entry.experiment( activity={'value':experiment_activity}))
            f.add_entry(dx.Entry.experiment( safety={'value':experiment_safety}))

            f.add_entry(dx.Entry.experimenter(name={'value':experimenter_name}))
            f.add_entry(dx.Entry.experimenter(role={'value':experimenter_role}))
            f.add_entry(dx.Entry.experimenter(affiliation={'value':experimenter_affiliation}))
            f.add_entry(dx.Entry.experimenter(address={'value':experimenter_address}))
            f.add_entry(dx.Entry.experimenter(phone={'value':experimenter_phone}))
            f.add_entry(dx.Entry.experimenter(email={'value':experimenter_email}))
            f.add_entry(dx.Entry.experimenter(facility_user_id={'value':experimenter_facility_user_id}))

            f.add_entry(dx.Entry.instrument(name={'value':instrument_name}))
            f.add_entry(dx.Entry.instrument(comment={'value':instrument_comment}))

            f.add_entry(dx.Entry.source(name={'value':source_name}))
            f.add_entry(dx.Entry.source(datetime={'value':source_datetime}))
            f.add_entry(dx.Entry.source(beamline={'value':source_beamline}))
            f.add_entry(dx.Entry.source(current={'value':source_current}))
            f.add_entry(dx.Entry.source(energy={'value':source_energy}))
            f.add_entry(dx.Entry.source(pulse_energy={'value':source_pulse_energy}))
            f.add_entry(dx.Entry.source(pulse_width={'value':source_pulse_width}))
            f.add_entry(dx.Entry.source(mode={'value':source_mode}))
            f.add_entry(dx.Entry.source(beam_intensity_incident={'value':source_beam_intensity_incident}))
            f.add_entry(dx.Entry.source(beam_intensity_transmitted={'value':source_beam_intensity_transmitted}))   

            f.add_entry(dx.Entry.attenuator( name={'value':attenuator_name}))
            f.add_entry(dx.Entry.attenuator( description={'value':attenuator_description}))
            f.add_entry(dx.Entry.attenuator( thickness={'value':attenuator_thickness}))
            f.add_entry(dx.Entry.attenuator( transmission={'value':attenuator_transmission}))
    
            f.add_entry(dx.Entry.monochromator( name={'value':monochromator_name}))
            f.add_entry(dx.Entry.monochromator( description={'value':monochromator_description}))
            f.add_entry(dx.Entry.monochromator( energy={'value':monochromator_energy}))
            f.add_entry(dx.Entry.monochromator( energy_error={'value':monochromator_energy_error}))
            f.add_entry(dx.Entry.monochromator( mono_stripe={'value':monochromator_mono_stripe}))
            
            f.add_entry(dx.Entry.mirror( name={'value':mirror_name}))
            f.add_entry(dx.Entry.mirror( description={'value':mirror_description}))

            f.add_entry(dx.Entry.detector(name={'value':detector_name}))
            f.add_entry(dx.Entry.detector(description={'value':detector_description}))
            f.add_entry(dx.Entry.detector(manufacturer={'value':detector_manufacturer}))
            f.add_entry(dx.Entry.detector(model={'value':detector_model}))
            f.add_entry(dx.Entry.detector(serial_number={'value':detector_serial_number}))
            f.add_entry(dx.Entry.detector(firmware_version={'value':detector_firmware_version}))
            f.add_entry(dx.Entry.detector(software_version={'value':detector_software_version}))
            f.add_entry(dx.Entry.detector(bit_dept={'value':detector_bit_dept}))
            f.add_entry(dx.Entry.detector(pixel_size_x={'value':detector_pixel_size_x}))
            f.add_entry(dx.Entry.detector(pixel_size_y={'value':detector_pixel_size_y}))
            f.add_entry(dx.Entry.detector(actual_pixel_size_x={'value':detector_actual_pixel_size_x}))
            f.add_entry(dx.Entry.detector(actual_pixel_size_y={'value':detector_actual_pixel_size_y}))
            f.add_entry(dx.Entry.detector(dimension_x={'value':detector_dimension_x}))
            f.add_entry(dx.Entry.detector(dimension_y={'value':detector_dimension_y}))
            f.add_entry(dx.Entry.detector(binning_x={'value':detector_binning_x}))
            f.add_entry(dx.Entry.detector(binning_y={'value':detector_binning_y}))
            f.add_entry(dx.Entry.detector(operating_temperature={'value':detector_operating_temperature}))
            f.add_entry(dx.Entry.detector(exposure_time={'value':detector_exposure_time}))
            f.add_entry(dx.Entry.detector(delay_time={'value':detector_delay_time}))
            f.add_entry(dx.Entry.detector(stabilization_time={'value':detector_stabilization_time}))
            f.add_entry(dx.Entry.detector(frame_rate={'value':detector_frame_rate}))
            f.add_entry(dx.Entry.detector(output_data={'value':detector_output_data}))
            f.add_entry(dx.Entry.detector(counts_per_joule={'value':detector_counts_per_joule}))
            f.add_entry(dx.Entry.detector(basis_vectors={'value':detector_basis_vectors}))
            f.add_entry(dx.Entry.detector(corner_position={'value':detector_corner_position}))

            f.add_entry(dx.Entry.roi(name={'value':detector_roi_name}))
            f.add_entry(dx.Entry.roi(description={'value':detector_roi_description}))
            f.add_entry(dx.Entry.roi(min_x={'value':detector_roi_min_x}))
            f.add_entry(dx.Entry.roi(min_y={'value':detector_roi_min_y}))
            f.add_entry(dx.Entry.roi(size_x={'value':detector_roi_size_x}))
            f.add_entry(dx.Entry.roi(size_y={'value':detector_roi_size_y}))

            f.add_entry(dx.Entry.objective(name={'value':objective_name}))
            f.add_entry(dx.Entry.objective(description={'value':objective_description}))
            f.add_entry(dx.Entry.objective(manufacturer={'value':objective_manufacturer}))
            f.add_entry(dx.Entry.objective(model={'value':objective_model}))
            f.add_entry(dx.Entry.objective(magnification={'value':objective_magnification}))
            f.add_entry(dx.Entry.objective(numerical_aperture={'value':objective_numerical_aperture}))

            f.add_entry(dx.Entry.scintillator(name={'value':scintillator_name}))
            f.add_entry(dx.Entry.scintillator(description={'value':scintillator_description}))
            f.add_entry(dx.Entry.scintillator(manufacturer={'value':scintillator_manufacturer}))
            f.add_entry(dx.Entry.scintillator(serial_number={'value':scintillator_serial_number}))
            f.add_entry(dx.Entry.scintillator(scintillating_thickness={'value':scintillator_scintillating_thickness}))
            f.add_entry(dx.Entry.scintillator(substrate_thickness={'value':scintillator_substrate_thickness}))

            f.add_entry(dx.Entry.sample_stack(name={'value':sample_stack_name}))
            f.add_entry(dx.Entry.sample_stack(description={'value':sample_stack_description}))

            f.add_entry(dx.Entry.sample_stack_setup(sample_x={'value':sample_stack_setup_sample_x}))
            f.add_entry(dx.Entry.sample_stack_setup(sample_y={'value':sample_stack_setup_sample_y}))
            f.add_entry(dx.Entry.sample_stack_setup(sample_z={'value':sample_stack_setup_sample_z}))
            f.add_entry(dx.Entry.sample_stack_setup(sample_xx={'value':sample_stack_setup_sample_xx}))
            f.add_entry(dx.Entry.sample_stack_setup(sample_zz={'value':sample_stack_setup_sample_zz}))

            f.add_entry(dx.Entry.interferometer(name={'value':interferometer_name}))
            f.add_entry(dx.Entry.interferometer(description={'value':interferometer_description}))

            f.add_entry(dx.Entry.interferometer_setup(grid_start={'value':interferometer_setup_grid_start}))
            f.add_entry(dx.Entry.interferometer_setup(grid_end={'value':interferometer_setup_grid_end}))
            f.add_entry(dx.Entry.interferometer_setup(number_of_grid_periods={'value':interferometer_setup_number_of_grid_periods}))
            f.add_entry(dx.Entry.interferometer_setup(number_of_grid_steps={'value':interferometer_setup_number_of_grid_steps}))

            f.add_entry(dx.Entry.process(name={'value':process_name}))

            f.add_entry(dx.Entry.acquisition(sample_position_x={'value':acquisition_sample_position_x}))
            f.add_entry(dx.Entry.acquisition(sample_position_y={'value':acquisition_sample_position_y})) 
            f.add_entry(dx.Entry.acquisition(sample_position_z={'value':acquisition_sample_position_z}))
            f.add_entry(dx.Entry.acquisition(sample_image_shift_x={'value':acquisition_sample_image_shift_x}))
            f.add_entry(dx.Entry.acquisition(sample_image_shift_y={'value':acquisition_sample_image_shift_y}))
            f.add_entry(dx.Entry.acquisition(image_theta={'value':acquisition_image_theta}))
            f.add_entry(dx.Entry.acquisition(scan_index={'value':acquisition_scan_index}))
            f.add_entry(dx.Entry.acquisition(scan_date={'value':acquisition_scan_date}))
            f.add_entry(dx.Entry.acquisition(image_date={'value':acquisition_image_date}))
            f.add_entry(dx.Entry.acquisition(time_stamp={'value':acquisition_time_stamp}))
            f.add_entry(dx.Entry.acquisition(image_number={'value':acquisition_image_number}))
            f.add_entry(dx.Entry.acquisition(image_exposure_time={'value':acquisition_image_exposure_time}))
            f.add_entry(dx.Entry.acquisition(image_is_complete={'value':acquisition_image_is_complete}))
            f.add_entry(dx.Entry.acquisition(shutter={'value':acquisition_shutter}))
            f.add_entry(dx.Entry.acquisition(image_type={'value':acquisition_image_type}))
            f.add_entry(dx.Entry.acquisition(start_date={'value':acquisition_start_date}))
            f.add_entry(dx.Entry.acquisition(end_date={'value':acquisition_end_date}))

            f.add_entry(dx.Entry.acquisition_setup(number_of_projections={'value':acquisition_setup_number_of_projections}))
            f.add_entry(dx.Entry.acquisition_setup(number_of_darks={'value':acquisition_setup_number_of_darks}))
            f.add_entry(dx.Entry.acquisition_setup(number_of_whites={'value':acquisition_setup_number_of_whites}))
            f.add_entry(dx.Entry.acquisition_setup(number_of_inter_whites={'value':acquisition_setup_number_of_inter_whites}))
            f.add_entry(dx.Entry.acquisition_setup(white_frequency={'value':acquisition_setup_white_frequency}))
            f.add_entry(dx.Entry.acquisition_setup(sample_in={'value':acquisition_setup_sample_in}))
            f.add_entry(dx.Entry.acquisition_setup(sample_out={'value':acquisition_setup_sample_out}))
            f.add_entry(dx.Entry.acquisition_setup(rotation_start_angle={'value':acquisition_setup_rotation_start_angle}))
            f.add_entry(dx.Entry.acquisition_setup(rotation_end_angle={'value':acquisition_setup_rotation_end_angle}))
            f.add_entry(dx.Entry.acquisition_setup(angular_step={'value':acquisition_setup_angular_step}))
            f.add_entry(dx.Entry.acquisition_setup(mode={'value':acquisition_setup_mode}))
            f.add_entry(dx.Entry.acquisition_setup(comment={'value':acquisition_setup_comment}))

            f.add_entry(dx.Entry.data(data={'value': data, 'units':'counts'}))
            f.add_entry(dx.Entry.data(data_white={'value': data_white, 'units':'counts'}))
            f.add_entry(dx.Entry.data(data_dark={'value': data_dark, 'units':'counts'}))
            f.add_entry(dx.Entry.data(theta={'value': theta, 'units':'degrees'}))

            f.close()
 
    else:
           print "Nothing to do ..."

if __name__ == "__main__":
    main()

