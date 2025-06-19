#pragma once

#include <Eigen/Core>
#include <vector>

std::vector<double> point_mesh_udf(const Eigen::MatrixXd &points,
                                   const Eigen::MatrixXd &verts,
                                   const Eigen::MatrixXi &faces);
